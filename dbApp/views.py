from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def about(request):
    return HttpResponse("aboot<br><a href='/'>back</a>")

def index(request):
    visited = 0
    template_name = 'index.html'
    contextual = ({'test': "hello again!",})
    contextual = ({'test': "hello!",})

    return render(request, template_name, contextual)

