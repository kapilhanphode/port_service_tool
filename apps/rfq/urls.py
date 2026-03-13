from django.urls import path
from .views import rfqs_view, create_rfq

urlpatterns = [
    path('', rfqs_view, name='rfqs'),
    path('create/', create_rfq, name='create_rfq'),
]