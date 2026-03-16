from django.urls import path
from .views import get_companies, get_company_details, create_company, update_company

urlpatterns = [
    path('', get_companies, name='get_company'),
    path('create/', create_company, name='create_company'),
    path('<int:pk>/', get_company_details, name='get_company_details'),
    path('<int:pk>/update/', update_company, name='update_company'),

]
