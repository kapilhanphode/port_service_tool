from django.db import models
from apps.accounts.models import User
from apps.rfq.models import RFQ

class Message(models.Model):
    rfq = models.ForeignKey(RFQ, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject