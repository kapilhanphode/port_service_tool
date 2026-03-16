from django.shortcuts import get_object_or_404
from core.utils.responses import success_response, error_response
from core.permissions.role_permissions import IsAdmin
from .models import Dispute
from .serializers import DisputeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin])
def dispute_list(request):
    disputes = Dispute.objects.all()
    serializer = DisputeSerializer(disputes, many=True)
    return success_response(
        data=serializer.data,
        message="Disputes fetched successfully"
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin])
def dispute_detail(request, pk):
    dispute = get_object_or_404(Dispute, pk=pk)
    serializer = DisputeSerializer(dispute)
    return success_response(
        data=serializer.data,
        message="Dispute details fetched successfully"
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdmin])
def raise_dispute(request):
    serializer = DisputeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(raised_by=request.user)
        return success_response(
            data=serializer.data,
            message="Dispute raised successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsAdmin])
def dispute_update(request, pk):
    dispute = get_object_or_404(Dispute, pk=pk)
    serializer = DisputeSerializer(dispute, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Dispute updated successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )