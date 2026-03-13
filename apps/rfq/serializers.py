from rest_framework import serializers
from .models import RFQ


class RFQSerializer(serializers.ModelSerializer):
    class Meta:
        model = RFQ
        fields = '__all__'
        read_only_fields = ["created_by"]