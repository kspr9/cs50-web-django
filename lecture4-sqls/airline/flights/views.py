from django.shortcuts import render

from  .models import Flight

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
    })