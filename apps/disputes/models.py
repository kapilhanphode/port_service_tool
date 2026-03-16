from django.db import models
from apps.purchase_orders.models import PurchaseOrder
from apps.accounts.models import User

class Dispute(models.Model):
    STATUS_CHOICES = (
    ('open', 'Open'),
    ('under_review', 'Under Review'),
    ('resolved', 'Resolved'),
    ('rejected', 'Rejected'),
    )
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dispute: {self.id}"
