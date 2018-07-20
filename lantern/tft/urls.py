from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

# from .views_2 import StartOrderViewSet


router = DefaultRouter()
# router.register('start', StartOrderViewSet, base_name='start')

app_name = 'tft'

urlpatterns = [
    # path('order/', include(router.urls)),
]