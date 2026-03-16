from django.urls import path
from .views import create_vessel, get_vessel_detail, get_vessels, update_vessel_detail

urlpatterns = [
    path('', get_vessels, name='get_vessels'),
    path('create/', create_vessel, name='create_vessel'),
    path('<int:pk>/', get_vessel_detail, name='get_vessel_detail'),
    path('<int:pk>/update/', update_vessel_detail, name='update_vessel_detail'),
]
