from django.urls import path
from .views import get_commissions, get_commission_detail, create_commission, update_commission


urlpatterns = [
    path('', get_commissions, name='get_commissions'),
    path('create/', create_commission, name='create_commission'),
    path('<int:pk>/', get_commission_detail, name='get_commission_detail'),
    path('<int:pk>/update/', update_commission, name='update_commission'),
]