from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.accounts.urls')),
    path('companies/', include('apps.companies.urls')),
    path('vessels/', include('apps.vessels.urls')),
    path('services/', include('apps.services.urls')),
    path('rfqs/', include('apps.rfq.urls')),
    path('quotations/', include('apps.quotations.urls')),
]