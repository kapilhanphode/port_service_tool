from django.urls import path
from .views import rfqs_view, rfq_detail_view, create_rfq, update_rfq

urlpatterns = [
    path('', rfqs_view, name='rfqs'),
    path('create/', create_rfq, name='create_rfq'),
    path('<int:pk>/', rfq_detail_view, name='rfq_detail_view'),
    path('<int:pk>/update/', update_rfq, name='update_rfq'),
]
