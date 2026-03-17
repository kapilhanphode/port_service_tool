from django.urls import path
from .views import quotation_list, quotation_detail, quotation_create, quotation_update, quotation_delete

urlpatterns = [
    path('', quotation_list, name='quotation_list'),
    path('create/', quotation_create, name='quotation_create'),
    path('<int:pk>', quotation_detail, name='quotation_detail'),
    path('<int:pk>/update/', quotation_update, name='quotation_update'),
    path('<int:pk>/delete/', quotation_delete, name='quotation_delete'),
]
