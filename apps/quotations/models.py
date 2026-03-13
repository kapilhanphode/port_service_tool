from django.db import models
from apps.accounts.models import User
from apps.companies.models import Company
from apps.rfq.models import RFQ

class Quotation(models.Model):
    STATUS_CHOICES = (
    ('submitted', 'Submitted'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('cancelled', 'Cancelled'),
    )
    rfq = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    supplier_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quotation {self.id} - {self.rfq.title}"
