from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Company(models.Model):
    COMPANY_TYPE_CHOICES = (
    ('client', 'Client'),
    ('supplier', 'Supplier'),
    )
    name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=100, choices=COMPANY_TYPE_CHOICES)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    imo_company_number = models.CharField(max_length=100, blank=True)
    verified = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
