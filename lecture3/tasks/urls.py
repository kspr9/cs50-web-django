from django.urls import path

from . import views


# this will allow to create <a href> in html files and link to the paths defined here
app_name = "tasks"
# for example when index page wants to visit 'add/' page, then the link is
# <a href="{% url 'tasks:add' %}">Add a New Task</a>

urlpatterns = [
    path("", views.index, name="index"),
    # when "/add/" page is visited, the add_task view function from 'tasks/views.py' will be run
    # and the add_task function will return the "tasks/add.html" page for the user
    path("add/", views.add_task, name="add"),
]
