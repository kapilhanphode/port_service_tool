from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == "client"

class IsSupplier(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == "supplier"

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class IsClientOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == "client" or request.user.is_staff