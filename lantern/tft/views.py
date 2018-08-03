from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, \
                                       DjangoModelPermissions, \
                                       DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import action
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from action.utils import create_action
from .models import Order, Audit, RecoverOrder, RecoverAudit
from .serializers import StartOrderSerializer, RetrieveStartOrderSerializer, \
                         ProductAuditSerializer, ChargeAuditSerializer, \
                         RecoverOrderSerializer, \
                         QcRecoverAuditSerializer, ProductRecoverAuditSerializer

from .utils import IsSameGroup, IsSameGroupRecoverOrder, IsMFGUser


class StartOrderViewSet(CreateModelMixin,
                        UpdateModelMixin,
                        # RetrieveModelMixin,
                        # ListModelMixin,
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
            return [IsAuthenticated(), DjangoModelPermissions()]
        elif self.action == 'update':
            return [IsAuthenticated(), IsSameGroup(), DjangoModelPermissions()]
        # elif self.action == 'retrieve':
        #     return [DjangoModelPermissionsOrAnonReadOnly()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), IsSameGroup(), DjangoModelPermissions()]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = self.perform_create(serializer)
        create_action(request.user, '开单', order)
        # headers = self.get_success_headers(serializer.data)
        return Response({'id': order.id, 'status_code': order.status, 'status': order.get_status_display()},
                        status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        create_action(request.user, '修改', instance)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({'id': instance.id, 'status_code': instance.status, 'status': instance.get_status_display()})

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class AuditViewSet(GenericViewSet):
    queryset = Audit.objects.all()
    # serializer_class = ProductAuditSerializer
    lookup_field = 'order_id'
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions()]

    def get_serializer_class(self):
        if self.action == 'product':
            return ProductAuditSerializer
        elif self.action == 'charge':
            return ChargeAuditSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'product':
            return [IsAuthenticated(), DjangoModelPermissions(), IsMFGUser()]
        return [permission() for permission in self.permission_classes]

    @action(methods=['post', 'put'], detail=False, url_path='product', url_name='product')
    def product(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        create_action(request.user, '审核', order)
        return Response({'id': order.id, 'status_code': order.status, 'status': order.get_status_display()})

    @action(methods=['post', 'put'], detail=False, url_path='charge', url_name='charge')
    def charge(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        create_action(request.user, '审核', order)
        return Response({'id': order.id, 'status_code': order.status, 'status': order.get_status_display()})


class RecoverOrderViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = RecoverOrder.objects.all()
    serializer_class = RecoverOrderSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), DjangoModelPermissions()]
        elif self.action == 'update':
            return [IsAuthenticated(), IsSameGroupRecoverOrder()]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        recover_order = self.perform_create(serializer)
        order = recover_order.order
        # status
        order.status = serializer.get_status(recover_order)
        order.save()

        # 这个地方有问题，两分钟内重复操作不记录
        create_action(request.user, '申请复机', order)

        headers = self.get_success_headers(serializer.data)
        return Response({'id': recover_order.id,
                         'order_id': order.id,
                         'status_code': order.status,
                         'status': order.get_status_display()},
                        status=status.HTTP_201_CREATED, headers=headers)

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

        return Response({'id': instance.id,
                         'status_code': instance.status,
                         'status': instance.get_status_display()})





class RecoverAuditViewSet(GenericViewSet):
    queryset = RecoverAudit.objects.all()
    serializer_class = QcRecoverAuditSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'qc':
            return QcRecoverAuditSerializer
        elif self.action == 'product':
            return ProductRecoverAuditSerializer
        return self.serializer_class

    @action(methods=['post'], detail=False, url_path='qc', url_name='qc')
    def qc(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recover_audit = serializer.save()
        recover_order = recover_audit.recover_order
        recover_order.order.status = serializer.get_status(recover_audit)
        recover_order.order.save()
        create_action(request.user, '审核', recover_order.order)

        return Response({'id': recover_order.id,
                         'order_id': recover_order.order.id,
                         'status': recover_order.order.get_status_display()},
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='product', url_name='product')
    def product(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recover_audit = serializer.save()
        recover_order = recover_audit.recover_order
        recover_order.order.status = serializer.get_status(recover_audit)
        recover_order.order.save()
        create_action(request.user, '审核', recover_order.order)

        return Response({'id': recover_order.id,
                         'order_id': recover_order.order.id,
                         'status': recover_order.order.get_status_display()},
                        status=status.HTTP_200_OK)


class OrderViewSet(ListModelMixin,
                   RetrieveModelMixin,
                   GenericViewSet):
    pass
