from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="tasks-index"),
    # when "/add/" page is visited, the add_task view function from 'tasks/views.py' will be run
    # and the add_task function will return the "tasks/add.html" page for the user
    path("add/", views.add_task, name="add-task"),
]
