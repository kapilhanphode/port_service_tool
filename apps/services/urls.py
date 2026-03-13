from django.urls import path
from .views import get_services, create_service


urlpatterns = [
    path('', get_services, name='get_services'),
    path('create/', create_service, name='create_service'),
]