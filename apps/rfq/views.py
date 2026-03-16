from django.shortcuts import get_object_or_404
from core.utils.responses import success_response, error_response
from core.permissions.role_permissions import IsClient
from core.pagination.pagination import StandardResultsPagination
from .models import RFQ
from .serializers import RFQSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsClient])
def rfqs_view(request):
    rfqs = RFQ.objects.all()

    # Filter by status if provided
    status_param = request.GET.get('status')
    if status_param:
        rfqs = rfqs.filter(status=status_param)

    # Search by title (or any other fields)
    search_param = request.GET.get('search')
    if search_param:
        rfqs = rfqs.filter(title__icontains=search_param)

    # Pagination
    paginator = StandardResultsPagination()
    paginated_rfqs = paginator.paginate_queryset(rfqs, request)
    serializer = RFQSerializer(paginated_rfqs, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsClient])
def rfq_detail_view(request, pk):
    rfq = get_object_or_404(RFQ, pk=pk)
    serializer = RFQSerializer(rfq)
    return success_response(
        data=serializer.data,
        message="RFQ detail fetched successfully"
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsClient])
def create_rfq(request):
    serializer = RFQSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return success_response(
            data=serializer.data,
            message="RFQ created successfully"
        )

    return error_response(
        message="Validation failed",
        error=serializer.errors
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsClient])
def update_rfq(request, pk):
    rfq = get_object_or_404(RFQ, pk=pk)
    serializer = RFQSerializer(instance=rfq, data=request.data, partial=True)
    if serializer.is_valid():
        print('serializer.error.....................', serializer.errors)
        serializer.save()
        return success_response(
            data=serializer.data,
            message="RFQ updated successfully"
        )

    return error_response(
        message="Validation failed",
        error=serializer.errors
    )
