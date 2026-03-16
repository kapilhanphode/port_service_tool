from django.db import models
from apps.quotations.models import Quotation
from apps.companies.models import Company


class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled'),
    )
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    client_company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='purchase_order_client_company')
    supplier_company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='purchase_order_supplier_company')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Purchase Orders'

    def __str__(self):
        return f"PO-{self.id}"