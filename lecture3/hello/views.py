from django.shortcuts import render
# need to import from standard django tools
from django.http import HttpResponse

# Create your views here.


def index(request):
    # import httpresponse
    return render(request, "hello/index.html")


def kaspar(request):
    # import httpresponse
    # using simple HttpResponse. Hard coded, static
    return HttpResponse("<head><title>Kaspar's View</title></head><body><h1>Hello Kaspar!</h1></body>")


def greet(request, name):
    # currently disabled in hello/urls.py as path, intefers with other_greet
    return HttpResponse(f"Hello, {name.capitalize()}!")


def other_greet(request, name):
    return render(request, "hello/greet.html", {
        # providing context for the current rendering request, provide a variable that can be used in html templates with {{ name }}
        "name": name.capitalize()
    })
