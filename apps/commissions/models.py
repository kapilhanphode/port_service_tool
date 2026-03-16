from django.db import models
from apps.purchase_orders.models import PurchaseOrder


class Commission(models.Model):
    order = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE)
    commission_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    commission_amount = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Commission: {self.id}'
