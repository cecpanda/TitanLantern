from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Order, StartOrder
from .serializers import CreateStartOrderSerializer
from .permissons import IsOpenOrderUser



class CreateStartOrder(CreateModelMixin, GenericAPIView):
    queryset = StartOrder.objects.all()
    serializer_class = CreateStartOrderSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)


'''
class OpenOrderViewSet(ListModelMixin,
                       CreateModelMixin,
                       RetrieveModelMixin,
                       UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = Order.objects.all()
    lookup_field = 'sn'
    serializer_class = OpenOrderSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        # if self.action == 'list' or self.action == 'retrieve':
            # return [permission() for permission in self.permission_classes]
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        elif self.action == 'create':
            # 任何已登录用户都有开单权限
            return [IsAuthenticated()]
        elif self.action == 'update' or self.action == 'partial_update':
            # 必须开单用户才能修改开单
            return [IsOpenOrderUser()]

    # 创建开单
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        open_order = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'order_sn': open_order.sn}, status=status.HTTP_201_CREATED, headers=headers)

    # 要重写，因为原来的没有 return
    def perform_create(self, serializer):
        return serializer.save()

    # 只能修改草稿箱中的开单
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.status == '0':
            return Response({'order_sn': instance.sn, 'msg': '只能修改草稿箱中的'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        open_order = self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({'order_sn': open_order.sn})

    def perform_update(self, serializer):
        return serializer.save()
'''