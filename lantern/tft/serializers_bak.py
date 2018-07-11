'''
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils import timezone

from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import Order, StartOrder, ReportFile, Remark, Eq, Lot, StartAudit
from account.serializers import UserSerializer


UserModel = get_user_model()


class CreateStartOrderSerializer(serializers.Serializer):
    draft = serializers.BooleanField(default=False)
    appl = serializers.HiddenField(default=serializers.CurrentUserDefault())
    eq = serializers.ListField(child=serializers.CharField(min_length=0, max_length=10))
    kind = serializers.CharField(min_length=0, max_length=30, required=False)
    step = serializers.CharField(min_length=0, max_length=100, required=False)
    found_time = serializers.DateTimeField()
    found_step = serializers.CharField(min_length=0, max_length=10, allow_blank=True)
    
    reason = serializers.CharField(min_length=0, max_length=100, required=False)
    users = serializers.ListField(child=serializers.CharField(min_length=0, max_length=128))
    charge_users = serializers.ListField(child=serializers.CharField(min_length=0, max_length=128))
    
    desc = serializers.CharField(min_length=0, max_length=300, allow_blank=True, required=False)
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    lot_num = serializers.IntegerField()
    lots = serializers.ListField(child=serializers.CharField(min_length=0, max_length=11))
    condition = serializers.CharField(min_length=0, max_length=200, allow_blank=True)
    deal = serializers.CharField(min_length=0, max_length=100)

    reports = serializers.ListField(child=serializers.FileField(allow_empty_file=True))
    remark = serializers.CharField(min_length=0, max_length=300, required=False)

    def validate(self, attrs):
        if attrs['start_time'] > attrs['end_time']:
            raise serializers.ValidationError('开始时间超过结束时间')

        return attrs

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
        return value

    def validate_users(self, value):
        # 不验证此用户是不是生产科的了
        for username in value:
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                raise serializers.ValidationError(f'{username} is not existed.')
        return value

    def validate_charge_users(self, value):
        for username in value:
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                raise serializers.ValidationError(f'{username} is not existed.')
        return value

    def create(self, validated_data):
        eq_list = validated_data.pop('eq')
        users = validated_data.pop('users')
        charge_users = validated_data.pop('charge_users')
        lots = validated_data.pop('lots')

        remark = validated_data.pop('remark')
        files = validated_data.pop('reports')

        # 验证 charge_users 是不是相关部门的人
        charge_group = Eq.objects.get(name=eq_list[0].upper()).kind.group
        for user_name in charge_users:
            user = UserModel.objects.get(username=user_name)
            if not charge_group in user.groups.all():
                raise serializers.ValidationError('责任工程人员和设备所属部门不符')

        order = Order.objects.create()
        start_order = StartOrder.objects.create(order=order, **validated_data)

        if not validated_data.get('draft'):
            order.status = '1'

        for eq_name in eq_list:
            eq = Eq.objects.get(name=eq_name.upper())
            start_order.eq.add(eq)

        for user_name in users:
            user = UserModel.objects.get(username=user_name)
            start_order.users.add(user)

        for charge_user_name in charge_users:
            user = UserModel.objects.get(username=charge_user_name)
            start_order.charge_users.add(user)

        for lot in lots:
            l = Lot.objects.create(name=lot)
            start_order.lots.add(l)

        if remark:
            remark = Remark.objects.create(order=order, content=remark)
        if files:
            for file in files:
                ReportFile.objects.create(order=order, file=file)

        return order.sn

    def update(self, instance, validated_data):
        # 这几个关系字段有点不太一样，提供就修改
        eq_list = validated_data.pop('eq')
        users = validated_data.pop('users')
        charge_users = validated_data.pop('charge_users')
        lots = validated_data.pop('lots')

        remark = validated_data.pop('remark')
        files = validated_data.pop('reports')

        instance.draft = validated_data.get('draft', instance.draft)
        instance.kind = validated_data.get('kind', instance.kind)
        instance.step = validated_data.get('step', instance.step)
        instance.found_time = validated_data.get('found_time', instance.found_time)
        instance.found_step = validated_data.get('found_step', instance.found_step)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.lot_num = validated_data.get('lot_num', instance.lot_num)
        instance.condition = validated_data.get('condition', instance.condition)
        instance.deal = validated_data.get('deal', instance.deal)

        # 验证 charge_users 是不是相关部门的人
        charge_group = Eq.objects.get(name=eq_list[0].upper()).kind.group
        for user_name in charge_users:
            user = UserModel.objects.get(username=user_name)
            if not charge_group in user.groups.all():
                raise serializers.ValidationError('责任工程人员和设备所属部门不符')

        if not validated_data.get('draft'):
            instance.order.status = '1'
            instance.order.save()

        if eq_list:
            instance.eq.clear()
            for eq_name in eq_list:
                eq = Eq.objects.get(name=eq_name.upper())
                instance.eq.add(eq)

        if users:
            instance.users.clear()
            for user_name in users:
                user = UserModel.objects.get(username=user_name)
                instance.users.add(user)

        if charge_users:
            instance.charge_users.clear()
            for charge_user_name in charge_users:
                user = UserModel.objects.get(username=charge_user_name)
                instance.charge_users.add(user)

        if lots:
            instance.lots.clear()
            for lot in lots:
                l = Lot.objects.create(name=lot)
                instance.lots.add(l)

        if remark:
            # instance.order.remarks.clear()
            # 上面的语法有问题，只有 m2m 正反都有 clear
            # 不用删除，重新创建
            remark = Remark.objects.create(order=instance.order, content=remark)

        if files:
            reports = instance.order.reports.all()
            for report in reports:
                report.delete()
            for file in files:
                ReportFile.objects.create(order=instance.order, file=file)

        try:
            instance.save()
            return instance.order.sn
        except:
            raise serializers.ValidationError('Update Failed')


class StartAuditSerializer(serializers.Serializer):
    order_sn = serializers.CharField()

    signer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    recipe_close = serializers.CharField(required=False)
    recipe_confirm = serializers.CharField(required=False)

    rejected = serializers.BooleanField(default=False)
    reason = serializers.CharField(min_length=0, max_length=100, required=False)

    remark = serializers.CharField(min_length=0, max_length=300, required=False)

    def validate_order_sn(self, value):
        try:
            Order.objects.get(sn=value)
        except:
            raise serializers.ValidationError(f'订单{value}不存在')
        return value

    def create(self, validated_data):
        order = Order.objects.get(sn=validated_data['order_sn'])
        start_audit, created = StartAudit.objects.get_or_create(order=order)
        # start_audit = StartAudit.objects.create(order=order)
        return start_audit

    def update(self, instance, validated_data):
        if instance.rejected:
            raise serializers.ValidationError('此单已被拒签')

        signer = validated_data.get('signer')

        charge_group = instance.order.startorder.eq.all()[0].kind.group
        try:
            prod_group = Group.objects.get(name='生产科')
        except:
            raise serializers.ValidationError('生产科不存在')

        if prod_group in signer.groups.all():
            if instance.p_signer:
                raise serializers.ValidationError('生产人员已签核')
            else:
                instance.p_signer = signer
                instance.p_time = timezone.now()
                instance.recipe_close = validated_data.get('recipe_close', instance.recipe_close)
                instance.recipe_confirm = validated_data.get('recipe_confirm', instance.recipe_confirm)
        elif signer in charge_group.user_set.all():
            if instance.c_signer:
                raise serializers.ValidationError('责任工程人员已签核')
            else:
                instance.c_signer = signer
                instance.c_time = timezone.now()
        else:
            raise serializers.ValidationError('审核人不是生产人员、责任工程人员')

        remark = validated_data.get('remark')
        if remark:
            remark = Remark.objects.create(order=instance.order, content=remark)

        instance.rejected = validated_data.get('rejected', instance.rejected)
        instance.reason = validated_data.get('reason', instance.reason)

        if instance.rejected:
            instance.order.status = '2'
        elif instance.p_signer and instance.c_signer:
            instance.order.status = '3'
        elif instance.p_signer or instance.c_signer:
            instance.order.status = '1'

        instance.save()

        return instance.order.sn
'''