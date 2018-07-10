from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import CreateStartOrder, UpdateStartOrder


router = DefaultRouter()

app_name = 'tft'

urlpatterns = [
    path('create/', CreateStartOrder.as_view()),
    path('update/<str:sn>/', UpdateStartOrder.as_view()),
    # path('startorder/audit/', )
]
