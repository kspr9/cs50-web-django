"""lecture3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# to include other apps urls
from django.urls import include
#from hello.views import index

urlpatterns = [
    path('admin/', admin.site.urls),

    # to add all hello related urls to this main urls file
    path('hello/', include("hello.urls")),

    # to add all hello related urls to this main urls file
    path('newyear/', include("newyear.urls")),
]
