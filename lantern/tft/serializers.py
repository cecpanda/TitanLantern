from django.db import transaction
from django.utils import timezone
from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Order, Eq, Lot, ID, Report, Remark


class StartOrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # group
    # charge_group
    # eq = serializers.ListField(label='停机设备', child=serializers.CharField(max_length=8), min_length=1)
    # lots = serializers.ListField(label='异常批次', child=serializers.CharField(max_length=14, min_length=8), required=False)
    charge_group = serializers.IntegerField(label='责任工程')
    reports = serializers.ListField(label='调查报告', child=serializers.FileField(), required=False)
    remark = serializers.CharField(label='生产批注', max_length=500, required=False)

    class Meta:
        model = Order
        fields = ('id', 'status', 'user',
                  'found_step', 'found_time', 'charge_group',
                  'eq', 'kind', 'step', 'reason',
                  'users', 'charge_users',
                  'desc', 'start_time', 'end_time', 'lot_num', 'lots',
                  'condition', 'defect_type',
                  'reports', 'remark')
        read_only_fields = ('id', 'status')

    # 改成字符串了
    # def validate_eq(self, value):
    #     # 是否已定义
    #     # 转换为大写
    #     # 去重
    #     # 同一科室
    #     try:
    #         first_charge_group = Eq.objects.get(name=value[0].upper()).kind.group
    #     except:
    #         raise serializers.ValidationError(f'{value[0]} 没有定义或没有对应的科室')
    #
    #     for name in value:
    #         name = name.upper()
    #         try:
    #             Eq.objects.get(name=name)
    #         except Eq.DoesNotExist:
    #             raise serializers.ValidationError(f'{name} is not defined.')
    #         try:
    #             charge_group = Eq.objects.get(name=name).kind.group
    #         except:
    #             raise serializers.ValidationError(f'{name} 未定义科室')
    #
    #         if charge_group != first_charge_group:
    #             raise serializers.ValidationError(f'{name} 与其他设备不属同一科室')
    #
    #     return set([name.upper() for name in value])

    def validate_charge_group(self, value):
        try:
            group = Group.objects.get(pk=value)
        except Exception as e:
            raise serializers.ValidationError('责任工程不存在')
        return value

    def get_id(self):
        '''id 生成
        根据开单工程生成 TEA-A01-001
        若开单用户是超级超级管理员或无科室人员，则使用 model 中默认的时间戳
        从 4000 开始
        '''
        group = self.get_group()
        id = ID.objects.create().id
        if not group:
            try:
                code = group.settings.code
            except Exception:
                return f'TEA-000-{id}'
            return f'TEA-{code}-{id}'
        return f'TEA-000-{id}'

    def get_group(self):
        # 根据 appl 得到 开单工程 group
        # appl 加入的第一个科室
        user = self.context['request'].user
        return user.groups.all().first()  # 返回最先加入的组，有可能为空，

    # def get_charge_group(self):
    #     # 根据 eq 得到 charge_group
    #     # self.initial_data 简直失了智， 你以为获取到的是 cak-01k，其实是 c
    #     first_eq_name = self.data['eq'][0].upper()
    #     try:
    #         eq = Eq.objects.get(name=first_eq_name)
    #     except:
    #         raise serializers.ValidationError(f'{first_eq_name}设备未定义')
    #     return eq.kind.group

    def create(self, validated_data):
        user = validated_data.get('user')
        status = '1'

        try:
            with transaction.atomic():
                order = Order.objects.create(id=self.get_id(),
                                             status=status,
                                             user=user,
                                             group=self.get_group(),  # 有可能为空
                                             found_step=validated_data.get('found_step'),
                                             found_time=validated_data.get('found_time'),
                                             # charge_group
                                             eq = validated_data.get('eq'),
                                             kind=validated_data.get('kind'),
                                             step=validated_data.get('step'),
                                             reason=validated_data.get('reason'),
                                             users=validated_data.get('users'),
                                             charge_users=validated_data.get('charge_users'),
                                             desc=validated_data.get('desc'),
                                             start_time=validated_data.get('start_time'),
                                             end_time=validated_data.get('end_time'),
                                             lot_num=validated_data.get('lot_num'),
                                             lots = validated_data.get('lots'),
                                             condition=validated_data.get('condition'),
                                             defect_type=validated_data.get('defect_type'))
                # # eq
                # for name in validated_data.get('eq'):
                #     eq = Eq.objects.get(name=name)
                #     order.eq.add(eq)

                # lots
                # lots = validated_data.get('lots')
                # if lots:
                #     for name in validated_data.get('lots'):
                #         lot = Lot.objects.create(name=name)
                #         order.lots.add(lot)

                # charge_group
                order.charge_group = Group.objects.get(pk=validated_data.get('charge_group'))
                order.save()

                # reports
                reports = validated_data.get('reports')
                if reports:
                    for file in reports:
                        Report.objects.create(order=order, file=file)

                # remark
                remark = validated_data.get('remark')
                if remark:
                    Remark.objects.create(user=user, order=order, content=remark)

        except Exception as e:
            raise serializers.ValidationError(f'出现错误{e}，提交数据被回滚。')

        return order.id

    def update(self, instance, validated_data):
        if instance.status != 1 or instance.status != 0:
            raise serializers.ValidationError('不能修改此订单')

        user = validated_data.get('user')

        try:
            with transaction.atomic():
                instance.mod_user = user
                instance.found_step = validated_data.get('found_step', instance.found_step)
                instance.found_time = validated_data.get('found_time', instance.found_time)
                # charge_group 不允许修改
                instance.eq = validated_data.get('eq', instance.eq)
                instance.kind = validated_data.get('kind', instance.kind)
                instance.step = validated_data.get('step', instance.step)
                instance.reason = validated_data.get('reason', instance.reason)
                instance.users = validated_data.get('users', instance.users)
                instance.charge_users = validated_data.get('charge_users', instance.charge_users)
                instance.desc = validated_data.get('desc', instance.desc)
                instance.start_time = validated_data.get('start_time', instance.start_time)
                instance.end_time = validated_data.get('end_time', instance.end_time)
                instance.lot_num = validated_data.get('lot_num', instance.lot_num)
                instance.lots = validated_data.get('lots', instance.lots)
                instance.condition = validated_data.get('condition', instance.condition)
                instance.defect_type = validated_data.get('defect_type', instance.defect_type)

                # reports
                # remark
        except Exception as e:
            raise serializers.ValidationError(f'出现错误{e}，提交数据被回滚。')

