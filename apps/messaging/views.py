from django.shortcuts import get_object_or_404
from core.utils.responses import success_response, error_response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from apps.messaging.models import Message
from .serializers import MessageSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return success_response(
        data=serializer.data,
        message="Messages fetched successfully"
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    serializer = MessageSerializer(message, many=False)
    return success_response(
        data=serializer.data,
        message="Message details fetched successfully"
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(sender=request.user)
        return success_response(
            data=serializer.data,
            message="Message sent successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    serializer = MessageSerializer(message, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(sender=request.user)
        return success_response(
            data=serializer.data,
            message="Message updated successfully"
        )
    return error_response(
        message="Validation failed",
        error=serializer.errors
    )