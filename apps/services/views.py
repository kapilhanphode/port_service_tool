from django.shortcuts import get_object_or_404
from core.utils.responses import success_response, error_response

from .models import Service
from .serializers import ServiceSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_services(request):
    services = Service.objects.filter(is_active=True)
    serializer = ServiceSerializer(services, many=True)

    return success_response(
        data=serializer.data,
        message="Services fetched successfully"
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    serializer = ServiceSerializer(service)

    return success_response(
        data=serializer.data,
        message="Service details fetched successfully"
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_service(request):
    serializer = ServiceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Service created successfully"
        )

    return error_response(
        message="Validation failed",
        error=serializer.errors
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    serializer = ServiceSerializer(instance=service, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Service updated successfully"
        )

    return error_response(
        message="Validation failed",
        error=serializer.errors
    )