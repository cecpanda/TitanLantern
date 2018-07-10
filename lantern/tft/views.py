from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, SAFE_METHODS, DjangoModelPermissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import APIException
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Order, StartOrder, StartAudit
from .serializers import CreateStartOrderSerializer, StartAuditSerializer
from .permissons import IsStartOrderAppl


class CreateStartOrder(CreateModelMixin, GenericAPIView):
    queryset = StartOrder.objects.all()
    serializer_class = CreateStartOrderSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_sn = self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        return Response({'order_sn': order_sn}, status=status.HTTP_201_CREATED)# , headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class UpdateStartOrder(UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    # queryset = StartOrder.objects.all()
    serializer_class = CreateStartOrderSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, IsStartOrderAppl]
    lookup_field = 'sn'

    # 只能修改草稿箱中的
    def get_object(self):
        # queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(Order, **filter_kwargs).startorder

        if not obj.draft:
            raise APIException(detail='只能修改和删除草稿箱中的订单', code=400)
            # return Response({'content', '只能修改和删除草稿箱中的订单'})

        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

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

        return Response({'order_sn': instance.order.sn})

    def perform_update(self, serializer):
        return serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.order.delete()
        # 因为级联删除，下面的不需要了
        # instance.delete()


class AuditStartOrder(CreateModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = StartAudit.objects.all()
    serializer_class = StartAuditSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def post(self, request, *args, **kwargs):
        pass

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

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
