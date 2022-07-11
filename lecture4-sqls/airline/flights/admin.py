from django.contrib import admin

from .models import Airport, Flight, Passenger

# Register your models here.

# with below class I am changing the way the flights list is displayed inside admin app
# must add the class when registering the site
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

# adding horizontal filtering options from default django admin options. 
# This can be seen under the admin/passengers > passenger detail view
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)