from django.urls import path
from .views import quotation_list, quotation_create


urlpatterns = [
    path('', quotation_list, name='quotation_list'),
    path('create/', quotation_create, name='quotation_create'),
]