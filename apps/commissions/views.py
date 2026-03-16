from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from core.utils.responses import success_response, error_response
from .models import Commission
from .serializers import CommissionSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_commissions(request):
    commissions = Commission.objects.all()
    serializer = CommissionSerializer(commissions, many=True)
    return success_response(
        data=serializer.data,
        message="Commissions fetched successfully"
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_commission_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    serializer = CommissionSerializer(commission)
    return success_response(
        data=serializer.data,
        message="Commission detail fetched successfully"
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_commission(request):
    serializer = CommissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Commission created successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_commission(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    serializer = CommissionSerializer(instance=commission, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Commission updated successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )