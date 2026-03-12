from django.shortcuts import render
from rest_framework import status

from .serializers import VesselSerializer
from .models import Vessel
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_vessel(request):
    serializer = VesselSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vessels(request):
    vessels = Vessel.objects.all()
    serializer = VesselSerializer(vessels, many=True)
    return Response(serializer.data)




