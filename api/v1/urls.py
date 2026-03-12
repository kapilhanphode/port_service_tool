from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.accounts.urls')),
    path('companies/', include('apps.companies.urls')),
    path('vessels/', include('apps.vessels.urls')),
]