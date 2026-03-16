from django.urls import path
from .views import get_services, get_service_detail, create_service, update_service

urlpatterns = [
    path('', get_services, name='get_services'),
    path('create/', create_service, name='create_service'),
    path('<int:pk>/', get_service_detail, name='get_service_detail'),
    path('<int:pk>/update/', update_service, name='update_service'),
]
