from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'realname', 'email',  'mobile', 'avatar', 'gender', 'birthday')
        extra_kwargs = {'password': {'write_only': True}}
