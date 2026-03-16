from django.shortcuts import get_object_or_404
from core.utils.responses import success_response, error_response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from .models import Company
from .serializers import CompanySerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return success_response(
        data=serializer.data,
        message="Companies fetched successfully"
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_company_details(request, pk):
    company = get_object_or_404(Company, pk=pk)
    serializer = CompanySerializer(company, many=False)
    return success_response(
        data=serializer.data,
        message="Company details fetched successfully"
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_company(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return success_response(
            data=serializer.data,
            message="Company created successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    serializer = CompanySerializer(company, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return success_response(
            data=serializer.data,
            message="Company updated successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )