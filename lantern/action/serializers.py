from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Action
from account.serializers import UserOfGroupSerializer


class ActionSerializer(serializers.ModelSerializer):
    # user = UserOfGroupSerializer()
    user = serializers.SerializerMethodField()
    target = serializers.SerializerMethodField()

    class Meta:
        model = Action
        fields = ('user', 'verb', 'target', 'created')

    def get_user(self, obj):
        return {'username': obj.user.username}

    def get_target(self, obj):
        # 此处显示用户时，不够优雅，最后要改
        data = {
            'id': obj.target.id,
            # 'url': self.context['request'].META['HTTP_HOST'] + obj.target.get_absolute_url()
            # 'url': self.context['request'].get_host()
            'url': self.context['request'].build_absolute_uri(obj.target.get_absolute_url())
        }
        return data
