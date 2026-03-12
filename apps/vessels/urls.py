from django.urls import path
from .views import create_vessel, get_vessels


urlpatterns = [
    path('', get_vessels, name='get_vessels'),
    path('create/', create_vessel, name='create_vessel'),
]