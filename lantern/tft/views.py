from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Order, Audit
from .serializers import StartOrderSerializer, RetrieveStartOrderSerializer, \
                         AuditSerializer
from .utils import IsSameGroup


class StartOrderViewSet(CreateModelMixin,
                        UpdateModelMixin,
                        RetrieveModelMixin,
                        ListModelMixin,
                        # DestroyModelMixin,
                        GenericViewSet):
    '''
    create:
        创建停机单

    update:
        修改同科室成员、尚未审核的订单

    retrieve
        获取订单

    list
        获取所有订单

    destroy
        删除订单
    '''
    queryset = Order.objects.all()
    serializer_class = StartOrderSerializer
    lookup_field = 'id'
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return StartOrderSerializer
        if self.action == 'update':
            return StartOrderSerializer
        if self.action == 'retrieve':
            return RetrieveStartOrderSerializer
        if self.action == 'list':
            return RetrieveStartOrderSerializer
        # 因为createserializer 影响了 retrieve 的 format=api
        # 所以用下面那个
        # return self.serializer_class
        return RetrieveStartOrderSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'update':
            return [IsAuthenticated(), IsSameGroup()]
        elif self.action == 'retrieve':
            return [IsAuthenticated()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), IsSameGroup()]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id = self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        return Response({'id': id}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({'id': instance.id})

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class AuditViewSet(CreateModelMixin,
                   ListModelMixin,
                   RetrieveModelMixin,
                   GenericViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    lookup_field = 'order_id'
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


from .serializers import OrderNextStepSerializer

class OrderNextStepViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderNextStepSerializer
