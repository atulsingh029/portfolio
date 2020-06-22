from django.shortcuts import render,HttpResponse,redirect
from .forms import MailingForm,VisitorForm
from django.core.mail import send_mail
from .models import Visitor,Contact,Carousel,ProjectCards


def home(request):
    success = ''
    try:
        if request.GET['q'] == 'success':
            success = "Thank you for contacting, I shall respond back soon to your provided email."
    except:
        pass
    mform = MailingForm()
    vform = VisitorForm()
    temp = ProjectCards.getProjectCards()

    twolists = [temp[0:int(len(temp)/2)],temp[int(len(temp)/2):int(len(temp))]]
    introtext = 'I am Atul Singh, a computer science student currently in 3rd year of graduation. ' \
                'The sections below highlight my experience in Computer Science - and it is forever growing! I have included relevant courses, my involvement in the CS community, and status on different coding websites.' \
                ' I have also included links to all of my research and projects.'
    introimage = 'https://atulsingh029.github.io/images/dp.jpg'
    context = {'contactform':mform, 'presenceform':vform, 'success':success,  'carousels':Carousel.getCarousel(),
               'list1':twolists[0], 'list2':twolists[1], 'introtext':introtext, 'introimage':introimage, }
    return render(request, 'base.html',context=context)

def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']+'\nSENDER : \n'+name+'\n'+email
        send_mail(subject,message,'atul.auth@gmail.com',['atulsinghash@gmail.com',],fail_silently=True)
        Contact.objects.create(email=email, name=name, subject=subject, message=message)
        reply_subject ='Re:'+subject
        reply_message = 'Hey '+name+",\nThank you for contacting. I have received your message, you will soon hear from me.\nAtul Singh\n\n\n<h6>Don't reply to this mail, this is system generated.</h6>"
        send_mail(reply_subject, reply_message, 'atul.auth@gmail.com', [email, ], fail_silently=True)
        return redirect('/?q=success')
    else:
        return redirect('/')

def presence(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        try:
            status = request.POST['subscribe']
            subscribe = True
        except:
            subscribe = False
        Visitor.objects.create(email=email, name=name, subscribe=subscribe)
        return redirect('/')
    else:
        return redirect('/')
