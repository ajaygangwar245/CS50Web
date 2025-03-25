from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

# def flight(request, flight_id):
#     # can use pk (primary key) instead of id
#     try: 
#         flight = Flight.objects.get(id=flight_id)
#     except:
#         return render(request, "flights/error.html", {
#             "id": flight_id
#         })
#     else:
#         return render(request, "flights/flight.html", {
#             "flight": flight,
#             "passengers": flight.passengers.all()
#         })

def flight(request, flight_id):
    # can use pk (primary key) instead of id
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })
    
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(id=flight_id)
        passenger = Passenger.objects.get(id=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights", args=(flight.id,)))

    
