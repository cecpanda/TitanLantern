from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import OpenOrderViewSet

router = DefaultRouter()
router.register('openorder', OpenOrderViewSet)

app_name = 'tft'

urlpatterns = [
    path('', include(router.urls)),
]