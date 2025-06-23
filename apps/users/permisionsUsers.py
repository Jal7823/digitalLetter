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
    
class IsStaffOrEmploye(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        # Se asegura de que esté autenticado y sea explícitamente staff o employe
        return bool(
            user
            and user.is_authenticated
            and (user.is_staff or user.role == "employe")
        )

