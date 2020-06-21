from django.shortcuts import render,HttpResponse

def blog(request):
    return HttpResponse("<h2> blog is under development, it will be available soon.</h2><p>Stay tuned for quality content on tech</p>")
