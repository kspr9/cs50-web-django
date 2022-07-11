from django.shortcuts import render
# for book function
from django.http import HttpResponseRedirect
from django.urls import reverse

from  .models import Flight, Passenger

#add request as parameter to be able to use the rendering function within a view
def index(request):
    return render(request, "flights/index.html", {
        # creating a flights variable that we can use in html page. 
        # when looping overs as for 'flight in flights', and also when accessing id as flight.id in the loop
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    # creating a flight variable that we can pass as html context variable in our return function below
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        # creating "flight" variable that we can use in html page
        "flight": flight,
        "passengers": flight.passengers.all(),
        # defining all passengers that are not on the flight ie excluding all passengers that have a flight 
        # 'flights' is something defined in index function above
        "non_passengers": Passenger.objects.exclude(flights=flight).all(),
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        # taking the contents of a text field from flight.html called "passenger" and getting the associated Passenger object
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # Passenger model has attribute "flights". this will add a flight
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id, )))
    
# suggestion: add delete_passenger function, ( possibly also add and delete flight )