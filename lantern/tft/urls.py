from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import StartOrderViewSet


router = DefaultRouter()
router.register('order/start', StartOrderViewSet, base_name='start')

app_name = 'tft'

urlpatterns = [
    path('', include(router.urls)),
]