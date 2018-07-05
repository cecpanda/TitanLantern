from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import CreateStartOrder


router = DefaultRouter()

app_name = 'tft'

urlpatterns = [
    path('create/', CreateStartOrder.as_view()),
]
