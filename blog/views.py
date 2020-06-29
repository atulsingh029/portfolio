from django.shortcuts import render,HttpResponse
from home.forms import VisitorForm,MailingForm
from .models import Blog
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog(request):
    blog_list = Blog.objects.filter(allowed=True)
    if len(blog_list) == 0:
        return HttpResponse('<h3>This page is empty (no content is posted) at this moment. Please come back later.</h3>')
    else:
        last = len(blog_list)-1
    banner_temp = blog_list[last]
    top3=[]
    latest = []

    for i in blog_list:
            if i.top3:
                top3.append(i)
            else:
                latest.append(i)
    top3.reverse()
    try:
        latest.pop()
    except:
        pass
    latest.reverse()
    paged = Paginator(latest,5)
    page = request.GET.get('page', 1)
    try:
        latest = paged.get_page(page)
    except PageNotAnInteger:
        latest = paged.get_page(1)
    except EmptyPage:
        latest = paged.get_page(paged.num_pages)


    banner = {'link': banner_temp.link, 'title': banner_temp.title, 'image': banner_temp.image,
              'subtitle': banner_temp.subtitle, 'datetime': banner_temp.datetime,
              'writer': banner_temp.writer, 'type': banner_temp.type}
    if len(banner) == 0:
        banner={'title':'This section is empty at this moment.'}
    if len(latest) == 0:
        latest=['This section is empty at this moment.']
    if len(top3) == 0:
        top3=['This section is empty at this moment.']
    mform = MailingForm()
    vform = VisitorForm()
    context = {'contactform':mform, 'presenceform':vform,'redirect_to':'blog','top3flinks':top3,'flinks':latest, 'banner':banner}
    return render(request, 'blog.html',context=context)
