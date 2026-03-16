from django.shortcuts import get_object_or_404
from core.utils.responses import success_response, error_response

from .serializers import VesselSerializer
from .models import Vessel
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vessels(request):
    vessels = Vessel.objects.all()
    serializer = VesselSerializer(vessels, many=True)
    return success_response(
        data=serializer.data,
        message="Vessels fetched successfully"
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_vessel_detail(request, pk):
    vessel = get_object_or_404(Vessel, pk=pk)
    serializer = VesselSerializer(vessel)
    return success_response(
        data=serializer.data,
        message="Vessel details fetched successfully"
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_vessel(request):
    serializer = VesselSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Vessel created successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_vessel_detail(request, pk):
    vessel = get_object_or_404(Vessel, pk=pk)
    serializer = VesselSerializer(vessel, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Vessel updated successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )