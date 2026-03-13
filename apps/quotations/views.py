from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Quotation
from .serializers import QuotationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def quotation_list(request):
    quotations = Quotation.objects.all()
    serializer = QuotationSerializer(quotations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def quotation_create(request):
    serializer = QuotationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(submitted_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
