from django.shortcuts import get_object_or_404
from django.db.models import Q
from core.utils.responses import success_response, error_response
from core.permissions.role_permissions import IsSupplier
from core.pagination.pagination import StandardResultsPagination
from .models import Quotation
from .serializers import QuotationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsSupplier])
def quotation_list(request):
    quotations = Quotation.objects.all()

    # Filter by status
    status_param = request.GET.get('status')
    if status_param:
        quotations = quotations.filter(status=status_param)

    # Search by RFQ title or notes
    search_param = request.GET.get('search')
    if search_param:
        quotations = quotations.filter(
            Q(rfq__title__icontains=search_param) | Q(notes__icontains=search_param)
        )

    # Pagination
    paginator = StandardResultsPagination()
    paginated_quotations = paginator.paginate_queryset(quotations, request)
    serializer = QuotationSerializer(paginated_quotations, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsSupplier])
def quotation_detail(request, pk):
    quotation = get_object_or_404(Quotation, pk=pk)
    serializer = QuotationSerializer(quotation)
    return success_response(
        data=serializer.data,
        message="Quotation details fetched successfully"
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsSupplier])
def quotation_create(request):
    serializer = QuotationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(submitted_by=request.user)
        return success_response(
            data=serializer.data,
            message="Quotation created successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsSupplier])
def quotation_update(request, pk):
    quotation = get_object_or_404(Quotation, pk=pk)
    serializer = QuotationSerializer(quotation, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Quotation updated successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )
