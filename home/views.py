from django.shortcuts import render, redirect
from .forms import MailingForm, SubscriberForm
from django.core.mail import send_mail
from .models import *
import random


def home(request):
    ip = get_client_ip(request)
    refer=''
    try:
        if request.META.get('HTTP_REFERER'):
            refer = request.META.get('HTTP_REFERER')
            if refer == '':
                refer = 'Anonymous'
        else:
            if request.GET['r']:
                refer = request.GET['r']
                if refer == '':
                    refer = 'Anonymous'
    except:
        refer = 'Anonymous'

    Logger.objects.create(ip=ip, refer=refer)
    profile = Profile.objects.get(email='atulsingh29@protonmail.com')
    ach_badges = Badge.objects.filter(allowed=True, type='achievement')
    tech_stack = Badge.objects.filter(allowed=True, type='tech-stack')
    contact_buttons = ContactIcon.objects.filter(profile=profile)
    c = Certification.objects.filter(allowed=True)
    if len(c) < 3:
        certifications = c
    else:
        certifications = random.sample(list(c), 3)
    print(certifications)
    context = {
        'title':'Atul Singh : Portfolio', 'contact_buttons':contact_buttons, 'profile':profile, 'achievements':ach_badges,
        'tech_stack':tech_stack, 'certifications' : certifications
    }
    return render(request, 'portfolio.html', context=context)


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
        send_mail(subject,message,'atul.auth@gmail.com', ['atulsinghash@gmail.com', ], fail_silently=True)
        Contact.objects.create(email=email, name=name, subject=subject, message=message)
        reply_subject ='Re:'+subject
        reply_message = 'Hey '+name+",\nThank you for contacting. I have received your message, you will hear from me soon.\nAtul" \
                                    " Singh\n\n\nDon't reply to this mail, this is system generated."
        send_mail(reply_subject, reply_message, 'atul.auth@gmail.com', [email, ], fail_silently=True)
        return redirect(redir+'/?refer=refer_success'+typ)
    else:
        return redirect('/')


def presence(request):
    if request.method == 'POST':
        if request.is_ajax():
            email = request.POST['email']
            name = request.POST['name']
            Visitor.objects.create(email=email, name=name, subscribe=False)
            return redirect(redirect)
    else:
        return redirect('/')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def collab(request):
    return render(request, 'collab.html')


def projects(request):
    return render(request, 'project.html')


def certifications(request):
    pass


def collab_form(request,id):
    pass