from rest_framework.permissions import BasePermission


# 请求用户是否为开单用户
class IsStartOrderUser(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj.user == request.user
        return  False


class IsSameGroup(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        # 只要有相同的组就可以
        if request.user:
            obj_groups = obj.user.groups.all()
            req_groups = request.user.groups.all()
            if set(obj_groups) & set(req_groups):
                return True
        return False
