from django.shortcuts import render
from home.forms import SubscriberForm, MailingForm
from .models import Blog, Tag, BlogSeries
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from home.models import ContactIcon, Contact, Profile


def blog(request):
    profile = Profile.objects.get(email='atulsingh29@protonmail.com')
    contact_icons = ContactIcon.objects.filter(profile=profile)

    blog_len = Blog.objects.count()
    tags = Tag.objects.all()
    series = BlogSeries.objects.all()
    if blog_len == 0:
        return render(request, 'blog/blog_404.html', context={'contact_buttons': contact_icons, "profile": profile})

    banner_temp = Blog.get_latest_blog()

    top = Blog.get_top_blogs()

    latest = Blog.get_latest_blogs(20)

    paged = Paginator(latest, 6)
    page = request.GET.get('page', 1)
    try:
        latest = paged.get_page(page)
    except PageNotAnInteger:
        latest = paged.get_page(1)
    except EmptyPage:
        latest = paged.get_page(paged.num_pages)

    main_story = {'linkkey': banner_temp.linkkey, 'title': banner_temp.title, 'image': banner_temp.image.url,
                  'subtitle': banner_temp.subtitle, 'datetime': banner_temp.datetime,
                  'writer': banner_temp.writer, 'type': banner_temp.type}

    mform = MailingForm()
    vform = SubscriberForm()

    page_context = {'page_title': 'Blog', 'navbar_title': ' Blog', 'logo_link': 'blog/', 'contactform': mform,
                    'presenceform': vform, 'redirect_to': 'blog'}

    context = {'top_stories': top, 'latest_stories': latest, 'main_story': main_story,
               'page_context': page_context, 'topics': tags, 'series': series,
               'contact_buttons': contact_icons, 'profile':profile,
               }
    return render(request, 'blog/blog.html', context=context)


def blogView(request):
    profile = Profile.objects.get(email='atulsingh29@protonmail.com')
    contact_icons = ContactIcon.objects.filter(profile=profile)
    goto = request.GET.get('to', '')
    obj = Blog.objects.filter(linkkey=goto, allowed=True)
    if len(obj) == 0:
        return render(request, template_name='blog/blog_404.html',context={'contact_buttons': contact_icons, "profile": profile})
    series = BlogSeries.objects.filter(blogs=obj[0])
    if len(series) == 0:
        series = ''
    else:
        series = series[0]

    try:
        o = obj[0]
        o.visit_count += 1
        o.save()
        out = {'title': obj[0].title, 'image': obj[0].image,
               'subtitle': obj[0].subtitle, 'datetime': obj[0].datetime,
               'writer': obj[0].writer, 'type': obj[0].type, 'text': obj[0].text,
               'safe': obj[0].allow_html, 'linkkey': obj[0].linkkey}
        title = obj[0].title
    except:
        return render(request, template_name='blog/blog_404.html',context={'contact_buttons': contact_icons, "profile": profile})
    tags = obj[0].tags.all()
    genre = obj[0].type
    recommended = Blog.objects.filter(allowed=True, type=genre, )
    recommended_list = []
    count = 0
    for i in recommended:
        if count == 4:
            break
        if i.linkkey == obj[0].linkkey:
            continue
        recommended_list.append(i)
        count = count + 1
    recommended_list.reverse()
    mform = MailingForm()
    sidetitle = ' Blog'
    logolink = 'blog/'
    page_context = {"title": obj[0].title+" by "+obj[0].writer.first_name }
    context = {'blog': out, 'contactform': mform, 'title': title, 'sidetitle': sidetitle, 'logolink': logolink,
               'flinks': recommended_list, 'series_name': series, 'tags': tags, 'contact_buttons': contact_icons,
               'profile': profile, 'page_context': page_context,
               }
    return render(request, 'blog/blogview.html', context=context)


def get(request, obj):
    profile = Profile.objects.get(email='atulsingh29@protonmail.com')
    contact_icons = ContactIcon.objects.filter(profile=profile)
    context = {
        'contact_buttons': contact_icons, 'profile': profile
    }
    if obj == 'search':
        key = request.GET.get('key')[:255]
        blogs = Blog.objects.filter(title__icontains=key, allowed=True)
        if len(blogs) == 0:
            blogs = Blog.objects.filter(subtitle__icontains=key, allowed=True)
        if len(blogs) == 0:
            blogs = Blog.objects.filter(text__icontains=key, allowed=True)
        paged = Paginator(blogs, 10)
        page = request.GET.get('page', 1)
        try:
            result = paged.get_page(page)
        except PageNotAnInteger:
            result = paged.get_page(1)
        except EmptyPage:
            result = paged.get_page(paged.num_pages)
        context.update({"res": str(len(blogs)) + " results found!", "results": result, "key":key})
        return render(request, template_name='blog/blog_search_result.html', context=context)
    elif obj == 'series':
        key = request.GET['key'][:255]
        context.update({"res": "Feature coming soon!","error_message":"Working on it!"})
        return render(request, template_name='blog/blog_search_result.html', context=context)
    else:
        key = request.GET['key'][:30]
        blogs = Blog.objects.filter(tags__name=key, allowed=True)
        paged = Paginator(blogs, 10)
        page = request.GET.get('page', 1)
        try:
            result = paged.get_page(page)
        except PageNotAnInteger:
            result = paged.get_page(1)
        except EmptyPage:
            result = paged.get_page(paged.num_pages)
        context.update({"res": str(len(blogs)) + " results found!", "results": result, "key": key})
        context.update({"res": key + " "+obj})
        return render(request, template_name='blog/blog_search_result.html', context=context)