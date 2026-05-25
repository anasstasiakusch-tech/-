from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменение/удаление разрешено владельцу или администратору
        return obj.owner == request.user or request.user.is_staff