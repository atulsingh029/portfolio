from django.shortcuts import render,HttpResponse,redirect
from .forms import MailingForm,VisitorForm
from django.core.mail import send_mail
from .models import Visitor,Contact,Carousel,ProjectCards,Tracking_Logger


def home(request):
    success = ''
    refer = ''
    ip = get_client_ip(request)
    try:
        if request.GET['refer'] == 'refer_success':
            success = "Thank you for contacting, I shall respond back soon to your provided email."
    except:
        pass
    try:
        if request.GET['refer']:
            refer = request.GET['refer']
            if refer == '':
                refer = 'Anonymous'
    except:
        refer = 'Anonymous'

    mform = MailingForm()
    vform = VisitorForm()
    temp = []
    for card in ProjectCards.getProjectCards():
        if card['allowed'] == True:
            temp.append(card)
    Tracking_Logger.objects.create(ip = ip, refer=refer)
    twolists = [temp[0:int(len(temp)/2)],temp[int(len(temp)/2):int(len(temp))]]
    introtext = 'I am Atul Singh, a computer science student currently in 3rd year of graduation. ' \
                'The sections below highlight my experience in Computer Science - and it is forever growing! I have included' \
                ' relevant courses, my involvement in the CS community, and status on different coding websites.' \
                ' I have also included links to all of my research and projects.'
    introimage = 'https://atulsingh029.github.io/images/dp.jpg'
    context = {'contactform':mform, 'presenceform':vform, 'success':success,  'carousels':Carousel.getCarousel(),
               'list1':twolists[0], 'list2':twolists[1], 'introtext':introtext, 'introimage':introimage, }
    return render(request, 'base.html',context=context)

def contact(request):
    try:
        redir = '/'+request.GET['redir']
        typ = '&type='+request.GET['type']
    except:
        redir = ''
        typ = ''
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']+'\n\nSENDER : \n'+name+'\n'+email
        send_mail(subject,message,'atul.auth@gmail.com',['atulsinghash@gmail.com',],fail_silently=True)
        Contact.objects.create(email=email, name=name, subject=subject, message=message)
        reply_subject ='Re:'+subject
        reply_message = 'Hey '+name+",\nThank you for contacting. I have received your message, you will hear from me soon.\nAtul" \
                                    " Singh\n\n\nDon't reply to this mail, this is system generated."
        send_mail(reply_subject, reply_message, 'atul.auth@gmail.com', [email, ], fail_silently=True)
        return redirect(redir+'/?refer=refer_success'+typ)
    else:
        return redirect('/')

def presence(request):
    try:
        redir = '/'+request.GET['redir']
        typ = '/?type='+request.GET['type']
    except:
        redir = '/'
        typ = ''
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        try:
            status = request.POST['subscribe']
            subscribe = True
        except:
            subscribe = False
        Visitor.objects.create(email=email, name=name, subscribe=subscribe)
        return redirect(redir+typ)
    else:
        return redirect('/')


def list_all(request):
    try:
        if request.GET['refer'] == 'refer_success':
            success = "Thank you for contacting, I shall respond back soon to your provided email."
    except:
        success = ''
    redirectto = 'list_all'
    try:
        type = request.GET['type']
    except:
        return redirect('/')
    if type == 'certificates':
        heading = ['Name', 'IssuedBy', 'Certificate']
        items = []
        out = Carousel.getCarousel()
        for i in out:
            if i['iscertificate']:
                temp = {'text1':i['name'], 'text2':i['issuedby'], 'link1':i['carouselapplink'],'btn1':'view certificate',}
                items.append(temp)
        mform = MailingForm()
        vform = VisitorForm()
        context = {'headings': heading, 'items': items, 'list_type': type, 'contactform':mform, 'presenceform':vform,
                   'redirect_to':redirectto, 'nav1':'Projects', 'navlink1':'/list_all/?type=projects', 'success':success,
                   }
        return render(request, 'list.html', context=context)
    elif type == 'projects':
        heading = ['Name', 'AppLink', 'SourceCode']
        items = []
        mform = MailingForm()
        vform = VisitorForm()
        out = ProjectCards.getProjectCards()
        for i in out:
            if i['applink'] is None:
                applink='#'
            else:
                applink = i['applink']
            sourcecode = i['sourcecode']
            temp={'text1':i['name'], 'link1':applink,'btn1':'open','link2':sourcecode,'btn2':'view','status1':i['appstatus'], 'status2':i['sourcestatus']}
            items.append(temp)
        context = {'headings': heading, 'items': items, 'list_type': type, 'contactform':mform, 'presenceform':vform,
                   'redirect_to':redirectto, 'nav1':'Certificates', 'navlink1':'/list_all/?type=certificates',
                   'success':success,}
        return render(request, 'list.html', context=context)
    else:
        return redirect('/')



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip