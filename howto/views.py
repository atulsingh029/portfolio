from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("<h1>How-To is under development, Stay tuned.</h1>")
