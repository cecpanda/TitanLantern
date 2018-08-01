from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import StartOrderViewSet, AuditViewSet, RecoverOrderViewSet, RecoverAuditViewSet


router = DefaultRouter()
router.register('order/start', StartOrderViewSet, base_name='start')
router.register('order/audit', AuditViewSet, base_name='audit')
router.register('order/recover', RecoverOrderViewSet, base_name='recover')
router.register('order/recover-audit', RecoverAuditViewSet, base_name='recover-audit')

app_name = 'tft'

urlpatterns = [
    path('', include(router.urls)),
]