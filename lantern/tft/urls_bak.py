'''
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views_bak import CreateStartOrder, UpdateStartOrder, AuditStartOrder


router = DefaultRouter()

app_name = 'tft'

urlpatterns = [
    path('create/', CreateStartOrder.as_view()),
    path('update/<str:sn>/', UpdateStartOrder.as_view()),
    path('startorder/audit/', AuditStartOrder.as_view()),
]
'''