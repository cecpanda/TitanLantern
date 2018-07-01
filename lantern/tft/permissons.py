from rest_framework.permissions import BasePermission


# 请求用户是否为开单用户
class IsOpenOrderUser(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.open_order_user == request.user
        return  False
