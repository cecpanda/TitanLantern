from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters


UserModel = get_user_model()

class UserFilter(filters.FilterSet):
    username = filters.CharFilter(name='username', lookup_expr='iexact')
    realname = filters.CharFilter(name='realname', lookup_expr='iexact')
    class Meta:
        model = UserModel
        fields = ['username', 'realname']