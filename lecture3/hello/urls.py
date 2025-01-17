from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ajay", views.ajay, name="ajay"),
    path("<str:name>", views.greet, name="greet")
]