from django.shortcuts import render
from rest_framework import status

from .models import RFQ
from .serializers import RFQSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rfqs_view(request):
    rfqs = RFQ.objects.all()
    serializer = RFQSerializer(rfqs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_rfq(request):
    serializer = RFQSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)