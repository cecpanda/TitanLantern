from django.conf import settings
from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException

from account.models import GroupSetting


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
        # if request.user:
        #     obj_groups = obj.user.groups.all()  # 开单人员所在的组，要考虑开单人huan组后的情况
        #     req_groups = request.user.groups.all()
        #     if set(obj_groups) & set(req_groups):
        #         return True
        if not obj.group:  # 没有开单工程，所有人都不可以修改
            return False
        if request.user:
            req_groups = request.user.groups.all()
            if obj.group in req_groups:
                return True
        return False


class RecoverOrderIsSameGroup(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.user:
            user_groups = obj.user.groups.all()
            mod_user_groups = request.user.groups.all()
            if set(user_groups) & set(mod_user_groups):
                return True
        return False


class IsMFGUser(BasePermission):
    def has_permission(self, request, view):
        try:
            mfg_code = settings.GROUP_CODE['TFT'].get('MFG')
            mfg = GroupSetting.objects.get(code=mfg_code).group
        except Exception as e:
            raise APIException(detail='没有找到生产科，请联系管理员确认', code=status.HTTP_403_FORBIDDEN)

        if mfg in request.user.groups.all():
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True
