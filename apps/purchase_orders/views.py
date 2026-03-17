from django.shortcuts import get_object_or_404
from django.db.models import Q
from core.utils.responses import success_response, error_response
from core.pagination.pagination import StandardResultsPagination
from core.permissions.role_permissions import IsClient, IsClientOrAdmin, IsAdmin
from core.throttles import LoginUserThrottle
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes, throttle_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsClientOrAdmin])
@throttle_classes([LoginUserThrottle])
def get_purchase_order(request):
    orders = PurchaseOrder.objects.filter(is_deleted=False)

    # Filter by status
    status_param = request.GET.get('status')
    if status_param:
        orders = orders.filter(status=status_param)

    # Search by client company or supplier company name
    search_param = request.GET.get('search')
    if search_param:
        orders = orders.filter(
            Q(client_company__name__icontains=search_param) |
            Q(supplier_company__name__icontains=search_param)
        )

    # Pagination
    paginator = StandardResultsPagination()
    paginated_orders = paginator.paginate_queryset(orders, request)
    serializer = PurchaseOrderSerializer(paginated_orders, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsClientOrAdmin])
def get_purchase_order_detail(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk, is_deleted=False)
    serializer = PurchaseOrderSerializer(order)
    return success_response(
        data=serializer.data,
        message="Purchase order details fetched successfully"
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsClientOrAdmin])
def create_purchase_order(request):
    serializer = PurchaseOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Purchase order created successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsClientOrAdmin])
def update_purchase_order(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk, is_deleted=False)
    serializer = PurchaseOrderSerializer(order, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Purchase order updated successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsClientOrAdmin])
def delete_purchase_order(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk, is_deleted=False)
    order.is_deleted = True
    order.save()
    return success_response(message="Purchase order deleted successfully")
