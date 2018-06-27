from django.shortcuts import render
from rest_framework import viewsets

from .models import HoldLot
from .serializers import HoldLotSerializer


class LotViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HoldLot.objects.all()
    serializer_class = HoldLotSerializer
