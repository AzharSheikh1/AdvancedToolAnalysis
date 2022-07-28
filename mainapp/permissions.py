from rest_framework import permissions
import pprint


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        pprint.pprint(
            f'{bool(request.user and request.user.is_superuser)} Azhar')
        return bool(request.user and request.user.is_superuser)


class FullDjangoModelPermission(permissions.DjangoModelPermissions):
    def __init__(self) -> None:
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
