from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User
from .serializers import UserSerializer, PasswordSerializer, GroupSerializer, \
                          GroupUserSerializer, UserUpdateSerializer
from .utils import UserPagination
from .filters import UserFilter


class UserViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    pagination_class = UserPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = UserFilter
    search_fields = ('$username', '$realname')
    ordering_fields = ('username', 'realname')

    @action(methods=['post'], detail=False, url_path='change-password', url_name='change_password', permission_classes=[IsAuthenticated])
    def change_password(self, request, pk=None):
        # 刚开始用 detail=True, self.get_object() 获得 user，这方法真特么傻
        user = self.request.user
        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if user.check_password(serializer.validated_data['old_password']):
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'status': 'ok'}, status.HTTP_202_ACCEPTED)
        return Response({'error': 'wrong password'}, status.HTTP_400_BAD_REQUEST)

    # 因为 UpdateModelMixin 的 url 不优雅，重新写
    @action(methods=['put'], detail=False, url_path='change-profile', url_name='change_profile', permission_classes=[IsAuthenticated])
    def change_profile(self, request, pk=None):
        user = self.request.user
        serializer = UserUpdateSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class GroupViewSet(ListModelMixin,
                   RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(methods=['GET', 'HEAD', 'OPTIONS'], detail=True, url_path='users', url_name='users')
    def users(self, request, pk=None):
        group = self.get_object()
        serializer = GroupUserSerializer(group)
        return Response(serializer.data)

