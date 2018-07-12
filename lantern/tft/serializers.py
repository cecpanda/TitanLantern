# -*- coding: utf-8 -*-

from django.db import transaction
from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from account.serializers import UserOfGroupSerializer, GroupSerializer
from .models import Eq, Lot, Order,  Report, Remark


UserModel = get_user_model()


class StartOrderSerializer(serializers.ModelSerializer):
    '''
    id
        根据 appl 的 group 自动生成，若无 group，则使用 model 中默认的
    status
        根据当前操作，自动决定
    appl
        当前登录用户
    group
        appl 所在的第一个组
    charge_group
        eq 所属的组
    users
        验证是否属于生产科
    charge_users
        验证是否为 charge_group 里的人员
    reports:
        可上传多个文件
    remark
        批注
        user 当前登录用户
    lots
        批次
    '''
    # id = serializers.CharField(label='编号', max_length=20,
    #                            validators=[UniqueValidator(queryset=Order.objects.all())])
    appl = serializers.HiddenField(default=serializers.CurrentUserDefault())
    eq = serializers.ListField(label='停机设备', child=serializers.CharField(max_length=10), min_length=1)
    users = serializers.ListField(label='通知生产人员', child=serializers.CharField(), min_length=1)
    charge_users = serializers.ListField(label='通知制程人员', child=serializers.CharField(), min_length=1)
    reports = serializers.ListField(label='调查报告', child=serializers.FileField(), required=False)
    remark = serializers.CharField(label='批注', max_length=300, required=False)
    lots = serializers.ListField(label='异常批次', child=serializers.CharField(max_length=12), required=False)

    class Meta:
        model = Order
        fields = ('id', 'status', 'appl', 'created', 'group', 'charge_group',
                  'eq', 'kind', 'step', 'found_time', 'found_step', 'reason',
                  'users', 'charge_users', 'desc', 'duration',
                  'lot_num', 'lots', 'condition', 'deal',
                  'reports', 'remark', 'draft')
        read_only_fields = ('id', 'status', 'created', 'group', 'charge_group')

    def validate_eq(self, value):
        '''验证 eq 是否已定义'''
        # 转化成大写字母
        # 去掉重复
        # 是否属于同一科室
        try:
            first_charge_group = Eq.objects.get(name=value[0].upper()).kind.group
        except:
            raise serializers.ValidationError(f'{value[0]} 未定义或未添加科室')

        for name in value:
            name = name.upper()
            try:
                Eq.objects.get(name=name)
            except Eq.DoesNotExist:
                raise serializers.ValidationError(f'{name} is not defined.')
            try:
                charge_group = Eq.objects.get(name=name).kind.group
            except:
                raise serializers.ValidationError(f'{name} 未定义科室')

            if charge_group != first_charge_group:
                raise serializers.ValidationError(f'{name} 与其他设备不属同一科室')

        return set([name.upper() for name in value])

    def validate_users(self, value):
        '''验证是否属于生产人员'''
        # 等生产科的名字确定后再写
        return value

    def validate_charge_users(self, value):
        '''验证是否属于 eq 所在的科室'''
        for name in value:
            try:
                user = UserModel.objects.get(username=name)
            except:
                raise serializers.ValidationError(f'{name} 不存在')

        return value

    # def validate_lots(self, value):
        # 不需要了

    def get_group(self):
        '''开单工程
        根据 appl 最先加入的科室，可能为空
        '''
        appl = self.context['request'].user
        return appl.groups.all().first()  # 返回最先加入的组，有可能为空，

    def get_charge_group(self):
        '''责任工程
        停机设备所在的科室
        '''
        # self.initial_data 简直失了智， 你以为获取到的是 cak-01k，其实是 c
        # first_eq_name = self.initial_data['eq'][0].upper()

        # 其实验证器已经变成大写了
        first_eq_name = self.data['eq'][0].upper()

        # 如果获取不到设备，验证器就报错了
        # 为了优雅点，还是验证以下
        try:
            eq = Eq.objects.get(name=first_eq_name)
        except:
            raise serializers.ValidationError(f'{first_eq_name}设备未定义')
        return eq.kind.group


    def get_id(self):
        ''' id 生成
        根据开单工程生成 TEA-01-001
        若开单用户是超级超级管理员或无科室人员，则使用 model 中默认的时间戳
        '''
        group = self.get_group()
        if group:
            try:
                code = group.settings.code
                last_order = Order.objects.filter(id__startswith=f'TEA-{code}-').order_by('id', 'created').last()

                if last_order:
                    last_id = last_order.id
                    last_id_num = last_id.split('-')[-1]
                    num = int(last_id_num) + 1
                    return f'TEA-{code}-{num}'
                else:
                    # 此科室第一次开单
                    return f'TEA-{code}-1'
            except:
                return timezone.localtime().strftime('%y%m%d-%H%M%S-%f')
        return timezone.localtime().strftime('%y%m%d-%H%M%S-%f')

    def create(self, validated_data):

        draft = True if validated_data.get('draft') else False
        status = '0' if draft else '1'

        try:
            with transaction.atomic():
                order = Order.objects.create(id=self.get_id(),  # 有默认值
                                             status=status,
                                             appl=validated_data.get('appl'),
                                             group=self.get_group(),  # 从 appl 中获取，可能为空
                                             charge_group=self.get_charge_group(),  #
                                             # eq  # 必选
                                             kind=validated_data.get('kind'),  # 必选
                                             step=validated_data.get('step'),  # 必选
                                             found_time=validated_data.get('found_time'),  # 必选
                                             found_step=validated_data.get('found_step'),  # 必选
                                             reason=validated_data.get('reason'),  # 必选
                                             # users  # 必选
                                             # charge_users  # 必选
                                             desc=validated_data.get('desc'),  # 必选
                                             duration=validated_data.get('duration'),  # 可为 None
                                             lot_num=validated_data.get('lot_num'),  # 可为 None
                                             # lots
                                             condition=validated_data.get('condition'),  # 必选
                                             deal=validated_data.get('deal', '停机'),  # 默认 "停机"
                                             draft=draft)
                for name in validated_data.get('eq'):
                    eq = Eq.objects.get(name=name)
                    order.eq.add(eq)
                for username in validated_data.get('users'):
                    user = UserModel.objects.get(username=username)
                    # ...
                for username in validated_data.get('charge_users'):
                    user = UserModel.objects.get(username=username)


        # lots 可能为空
        lots = validated_data.get('lots')
        if lots:
            for name in validated_data.get('lots'):
                lot = Lot.objects.create(name=name)
                # 。。。



        reports = validated_data.get('reports')
        if reports:
            for file in reports:
                Report.objects.create(order='', file=file)

        remark = validated_data.get('remark')
        if remark:
            Remark.objects.create(user=appl, order='', content=remark)



class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = "__all__"

class RemarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Remark
        fields = "__all__"


class ListStartOrderSerializer(serializers.ModelSerializer):
    appl = UserOfGroupSerializer()
    group = GroupSerializer()
    charge_group = GroupSerializer()
    users = UserOfGroupSerializer(many=True)
    charge_users = UserOfGroupSerializer(many=True)
    reports = ReportSerializer(many=True)
    remarks = RemarkSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
        depth = 2
