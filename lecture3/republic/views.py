from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "republic/index.html", {
        "republicday": now.day == 26 and now.month == 1 
        # to check true
        # "republicday": True
    })