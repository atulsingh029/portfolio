from django.shortcuts import render,HttpResponse,redirect
from .forms import MailingForm,VisitorForm
from django.core.mail import send_mail
from .models import Visitor,Contact,Carousel


def home(request):
    success = ''
    try:
        if request.GET['q'] == 'success':
            success = "Thank you for contacting, I shall respond back soon to your provided email."
    except:
        pass
    mform = MailingForm()
    vform = VisitorForm()
    return render(request, 'base.html',context={'contactform':mform, 'presenceform':vform, 'success':success,  'carousels':Carousel.getCarousel()})

def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']+'\nSENDER : \n'+name+'\n'+email
        send_mail(subject,message,'atul.auth@gmail.com',['atulsinghash@gmail.com',],fail_silently=True)
        Contact.objects.create(email=email, name=name, subject=subject, message=message)
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
