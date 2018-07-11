from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UserSerializer, PasswordSerializer, GroupSerializer, \
                         GroupUserSerializer, UserUpdateSerializer
from .utils import UserPagination
from .filters import UserFilter


UserModel = get_user_model()


class UserViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    pagination_class = UserPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = UserFilter
    search_fields = ('$username', '$realname')
    ordering_fields = ('username', 'realname')

    def get_serializer_class(self):
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )
        if self.action == 'change_password':
            return PasswordSerializer
        if self.action == "change_profile":
            return UserUpdateSerializer
        return self.serializer_class

    @action(methods=['post'], detail=False, url_path='change-password',
            url_name='change_password', permission_classes=[IsAuthenticated])
    def change_password(self, request):
        # 刚开始用 detail=True, self.get_object() 获得 user，这方法真特么傻
        user = request.user
        print('============================')
        print('user:', user)
        print('reqests:', request)
        print('data:', request.data)
        print('============================')
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        if user.check_password(serializer.validated_data.get('old_password')):
            user.set_password(serializer.validated_data.get('new_password'))
            user.save()
            return Response({'status': 'ok'}, status.HTTP_202_ACCEPTED)
        return Response({'error': 'wrong password'}, status.HTTP_400_BAD_REQUEST)

    # 因为 UpdateModelMixin 的 url 不优雅，重新写，
    # 而且在此视图里比较难做到谁登录谁修改
    @action(methods=['put'], detail=False, url_path='change-profile',
            url_name='change_profile', permission_classes=[IsAuthenticated])
    def change_profile(self, request):
        user = self.request.user
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class GroupViewSet(ListModelMixin,
                   RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(methods=['GET'], detail=True, url_path='users', url_name='users')
    def users(self, request, pk=None):
        group = self.get_object()
        serializer = GroupUserSerializer(group)
        return Response(serializer.data)
