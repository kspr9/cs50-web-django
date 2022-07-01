from django.shortcuts import render

tasks = ['foo', 'bar', 'baz']
# Create your views here.


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add_task(request):
    return render(request, "tasks/add.html")
