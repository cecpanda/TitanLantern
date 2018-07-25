from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import StartOrderViewSet, AuditViewSet


router = DefaultRouter()
router.register('order/start', StartOrderViewSet, base_name='start')
router.register('order/audit', AuditViewSet, base_name='audit')

app_name = 'tft'

urlpatterns = [
    path('', include(router.urls)),
]