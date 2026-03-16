from django.urls import path
from .views import get_messages, get_message_detail, send_message, update_message

urlpatterns = [
    path('', get_messages, name='get_messages'),
    path('send/', send_message, name='send_message'),
    path('<int:pk>/', get_message_detail, name='get_message_detail'),
    path('<int:pk>/update/', update_message, name='update_message'),
]
