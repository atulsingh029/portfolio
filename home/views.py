from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *
import random


def home(request):
    ip = get_client_ip(request)
    refer = ''
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
    projects = Project.objects.filter(allowed=True)
    page_context = {"title": "Atul Singh : Portfolio"}
    context = {
        'title': 'Atul Singh : Portfolio', 'contact_buttons': contact_buttons, 'profile': profile,
        'achievements': ach_badges, 'page_context':page_context,
        'tech_stack': tech_stack, 'certifications': certifications, 'projects': projects
    }
    return render(request, 'portfolio/portfolio.html', context=context)


def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message'] + '\n\nSENDER : \n' + name + '\n' + email
        send_mail(subject, message, 'atul.auth@gmail.com', ['atulsinghash@gmail.com', ], fail_silently=True)
        Contact.objects.create(email=email, name=name, subject=subject, message=message)
        reply_subject = 'Re:' + subject
        reply_message = 'Hey ' + name + ",\nThank you for contacting. I have received your message, you will hear from me soon.\nAtul" \
                                        " Singh\n\n\nDon't reply to this mail, this is system generated."
        send_mail(reply_subject, reply_message, 'atul.auth@gmail.com', [email, ], fail_silently=True)
        return redirect(redirect + '/?refer=refer_success')
    else:
        return render(request, template_name='portfolio/collab.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def certifications(request):
    obj_queryset = Certification.objects.filter(allowed=True)
    return HttpResponse("WORKING ON IT")


def view_project(request, id):
    project = []
    profile = Profile.objects.get(email='atulsingh29@protonmail.com')
    contact_icons = ContactIcon.objects.filter(profile=profile)
    obj_queryset = Project.objects.filter(id=id)
    if len(obj_queryset) != 0:
        project = obj_queryset[0]
    tech_stack = TechStack.objects.filter(project=project)
    screenshots = ProjectScreenshot.objects.filter(project=project)
    docs = ProjectRelatedDoc.objects.filter(project=project, type='public')
    page_context = {"title": "Project : "+project.name+" @AtulSingh"}
    context = {"project": project, "tech_stack": tech_stack, 'contact_buttons': contact_icons, 'profile': profile,
               "screenshots": screenshots, 'page_context': page_context, 'docs': docs,
               }
    return render(request, template_name='portfolio/project.html', context=context)


def resume(request):
    return HttpResponse("Work in progress")
