# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Eq, Order


class StartOrderSerializer(serializers.ModelSerializer):
    '''
    order_sn
    appl
    created
    group
    charge_group
    users
    charge_users
    lots
    '''
    id = serializers.CharField(label='编号', max_length=20,
                               validators=[UniqueValidator(queryset=Order.objects.all())])
    appl = serializers.HiddenField(default=serializers.CurrentUserDefault())
    eq = serializers.ListField(child=serializers.CharField(max_length=10))

    class Meta:
        model = Order
        fields = ('id', 'status', 'draft', 'appl', 'eq', 'kind', 'step',
                  'found_time', 'found_step', 'reason', # 'users', 'charge_users',
                  'desc', 'duration', 'lot_num', 'lots', 'condition', 'deal')

    def validate_eq(self, value):
        # eq 不能为空，但 ListField 无法验证
        if not value:
            raise serializers.ValidationError('eq must be included.')
        # 验证 eq 是否已定义
        for name in value:
            try:
                name = name.upper()
                Eq.objects.get(name=name)
            except Eq.DoesNotExist:
                raise serializers.ValidationError(f'{name} is not defined.')
        return eq

    @property
    def group(self):
        '''开单工程， appl 所在的科室'''
        appl = self.context['request'].user
        return appl.groups.all().first()  # 返回最先加入的组，有可能为空，

    @property
    def charge_group(self):
        '''责任工程，停机设备所在的科室'''
        pass

    @property
    def order_sn(self):
        pass
