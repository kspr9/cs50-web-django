from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = []
# Create your views here.

# creating a class NewTaskForm - builds the form that is used in add.html. Giving add.html access
# to this constructor is done in add_task function below


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # 'task' refers to NewTaskForms variable 'task'
            task = form.cleaned_data["task"]
            # here appended task refers to the task variable defined one row up
            # tasks.append(task) # instead of appending tasks we need to change this
            # this is coming from index function return context
            request.session["tasks"] += [task]
            # if a task is added, redirect to list of tasks ie index page
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        # give 'tasks/add.html' template access to a variable called 'form' and link it to
        # form builder class above
        "form": NewTaskForm()
    })
