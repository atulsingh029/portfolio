from django.shortcuts import render,HttpResponse
from home.forms import VisitorForm,MailingForm


def blog(request):
    mform = MailingForm()
    vform = VisitorForm()
    context = {'contactform':mform, 'presenceform':vform,'redirect_to':'blog'}
    return render(request, 'blog.html',context=context)
