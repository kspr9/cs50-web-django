from django.urls import path
# to use the index function we need to import the view module
from . import views

urlpatterns = [
    # to connect default route for this app "hello/" to the index function from hello/views.py
    path("", views.index, name="index"),
    # added a separate view for "hello/kaspar"
    path("kaspar", views.kaspar, name="kaspar-view"),
    # disabling atm since intefers with other_greet below
    #path("<str:name>", views.greet, name="greet"),
    path("<str:name>", views.other_greet, name="other_greet"),
]
