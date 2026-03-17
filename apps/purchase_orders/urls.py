from django.urls import path
from .views import get_purchase_order, get_purchase_order_detail, create_purchase_order, update_purchase_order, delete_purchase_order

urlpatterns = [
    path('', get_purchase_order, name='purchase_order'),
    path('create/', create_purchase_order, name='create_purchase_order'),
    path('<int:pk>/', get_purchase_order_detail, name='get_purchase_order_detail'),
    path('<int:pk>/update/', update_purchase_order, name='update_purchase_order'),
    path('<int:pk>/delete/', delete_purchase_order, name='delete_purchase_order'),
]
