from rest_framework.permissions import BasePermission


# 请求用户是否为开单用户
class IsStartOrderAppl(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.appl == request.user
        return  False
