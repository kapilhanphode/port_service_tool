from django.urls import path
from .views import dispute_list, dispute_detail, raise_dispute, dispute_update

urlpatterns = [
    path('', dispute_list, name='dispute_list'),
    path('raise/', raise_dispute, name='raise_dispute'),
    path('<int:pk>/', dispute_detail, name='dispute_detail'),  # GET detail
    path('<int:pk>/update/', dispute_update, name='dispute_update'),  # PATCH update
]
