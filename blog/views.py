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
            if i == banner_temp:
                continue
            if i.top3:
                top3.append(i)
            else:
                latest.append(i)
    top3.reverse()

    latest.reverse()
    paged = Paginator(latest,5)
    page = request.GET.get('page', 1)
    try:
        latest = paged.get_page(page)
    except PageNotAnInteger:
        latest = paged.get_page(1)
    except EmptyPage:
        latest = paged.get_page(paged.num_pages)


    banner = {'linkkey': banner_temp.linkkey, 'title': banner_temp.title, 'image': banner_temp.image,
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
    title = 'Blog'
    sidetitle = ' Blog'
    logolink = 'blog/'
    context = {'contactform':mform, 'title':title, 'sidetitle':sidetitle, 'logolink':logolink,
               'presenceform':vform,'redirect_to':'blog','top3flinks':top3,'flinks':latest,
               'banner':banner}
    return render(request, 'blog.html',context=context)


def blogView(request):
    goto = request.GET.get('to','')
    obj = Blog.objects.filter(linkkey=goto)
    try:
        out = {'title': obj[0].title, 'image':obj[0].image,
                  'subtitle': obj[0].subtitle, 'datetime': obj[0].datetime,
                  'writer': obj[0].writer, 'type': obj[0].type, 'text':obj[0].text}
        title = obj[0].title
    except:
        out = {'subtitle':'blog not found.'}
        title = '404 blog not found'
    mform = MailingForm()
    sidetitle = ' Blog'
    logolink = 'blog/'
    context = {'blog':out,'contactform':mform, 'title':title, 'sidetitle':sidetitle, 'logolink':logolink}
    return render(request,'blogview.html',context=context)