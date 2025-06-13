from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff == True)


class IsEmploye(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'employe')


class IsBoss(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'boos')