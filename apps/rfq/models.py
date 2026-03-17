from django.db import models
from apps.companies.models import Company
from apps.services.models import Service
from apps.vessels.models import Vessel
from apps.accounts.models import User
from core.models import BaseModel


class RFQ(BaseModel):
    STATUS_CHOICES = (
    ('open', 'Open'),
    ('evaluating', 'Evaluating'),
    ('closed', 'Closed'),
    ('canceled', 'Canceled'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    port = models.CharField(max_length=10, blank=True, null=True)
    deadline = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'RFQs'
        verbose_name = 'RFQ'

    def __str__(self):
        return self.title
