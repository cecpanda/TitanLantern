from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, GroupViewSet

app_name = 'account'

router = DefaultRouter()
router.register('user', UserViewSet, base_name='user')
router.register('group', GroupViewSet, base_name='group')


urlpatterns = [
    path('', include(router.urls))
]
