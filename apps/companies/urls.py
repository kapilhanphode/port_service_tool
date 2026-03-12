from django.urls import path
from .views import get_companies, create_company

urlpatterns = [
    path('', get_companies, name='get_company'),
    path('create/', create_company, name='create_company'),
]