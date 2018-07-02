from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import serializers


UserModel = get_user_model()


class JwtResponseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class UserOfGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'realname', 'email',  'mobile', 'phone', 'avatar', 'gender', 'birthday')

class GroupUserSerializer(serializers.ModelSerializer):
    user_set = UserOfGroupSerializer(many=True)
    class Meta:
        model = Group
        fields = ('id', 'name', 'user_set')


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = UserModel
        fields = ('username', 'realname', 'email',  'mobile', 'phone', 'avatar',
                  'gender', 'birthday', 'groups', 'last_login', 'date_joined')
        read_only_fields = ('username',)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'realname', 'email',  'mobile', 'phone', 'avatar',
                  'gender', 'birthday',)
        read_only_fields = ('username',)


class PasswordSerializer(serializers.Serializer):
    old_password =  serializers.CharField(style={'input_type': 'password'})
    new_password = serializers.CharField(style={'input_type': 'password'})
