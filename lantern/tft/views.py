# -*- coding: utf-8 -8-

from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Order
from .serializers import StartOrderSerializer, ListStartOrderSerializer


class StartOrderViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = StartOrderSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        assert self.serializer_class is not None, (
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method."
                % self.__class__.__name__
        )
        if self.action == 'list':
            return ListStartOrderSerializer
        if self.action == 'create':
            return StartOrderSerializer
        return self.serializer_class
