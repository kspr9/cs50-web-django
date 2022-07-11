# for implementing the login-logout procedure
from django.contrib.auth import authenticate, login, logout
# standard import for rendering views
from django.shortcuts import render
# for redirecting user to another url
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import urls

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        # redirects the user to 'login' path/route in urlpatterns
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        # takes the input names from login.html
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticates the user with inputted values
        user = authenticate(request, username=username, password=password)
        # checks for correctness
        if user is not None:
            # standard django function to login users
            login(request, user)
            # if condition is met, redirect the user back to index route
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "users/login.html")

def logout_view(request):
    # standard django function to logout users
    # after this the user will be unauthenticated in the session and thus "login.html" 
    # will also display the message
    logout(request)
    return render(request, "users/login.html", {
                "message": "Logged out."
            })