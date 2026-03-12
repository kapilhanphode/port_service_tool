from django.db import models
from apps.companies.models import Company

class Vessel(models.Model):
    VESSEL_TYPES = (
    ('bulk_carrier', 'Bulk Carrier'),
    ('tanker', 'Tanker'),
    ('container', 'Container'),
    ('passenger', 'Passenger'),
    )
    name = models.CharField(max_length=200)
    imo_number = models.CharField(max_length=10, unique=True)
    vessel_type = models.CharField(max_length=20, choices=VESSEL_TYPES)
    flag_state = models.CharField(max_length=20)
    year_built = models.IntegerField()
    gross_tonnage = models.IntegerField()
    classification_society = models.CharField(max_length=20)
    operational_status = models.CharField(max_length=20, default='in_service')
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


