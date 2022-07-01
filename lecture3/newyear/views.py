from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        # value of "newyear" variable is going to be True only if month == 1 and day == 1
        "newyear": now.month == 1 and now.day == 1
    })
