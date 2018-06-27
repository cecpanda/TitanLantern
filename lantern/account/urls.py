from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

app_name = 'account'

router = DefaultRouter()
router.register('user', UserViewSet)


urlpatterns = [
  path('', include(router.urls))
]
