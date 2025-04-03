from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    # we can use pk (primary key) instead of id
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        # passengers that are on flight
        "passengers": flight.passengers.all(),
        # passengers that are not on flight (or excluding that are on flight)
        "non_passengers": Passenger.objects.exclude(flights=flight).all()  
    })
    
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(id=flight_id)
        passenger = Passenger.objects.get(id=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

