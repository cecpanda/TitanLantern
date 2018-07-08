from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import Order, StartOrder, ReportFile, Remark, Eq, Lot
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
    remark = serializers.CharField(min_length=0, max_length=300)

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

        instance.eq.clear()
        for eq_name in eq_list:
            eq = Eq.objects.get(name=eq_name.upper())
            instance.eq.add(eq)

        instance.users.clear()
        for user_name in users:
            user = UserModel.objects.get(username=user_name)
            instance.users.add(user)

        instance.charge_users.clear()
        for charge_user_name in charge_users:
            user = UserModel.objects.get(username=charge_user_name)
            instance.charge_users.add(user)

        instance.lots.clear()
        for lot in lots:
            l = Lot.objects.create(name=lot)
            instance.lots.add(l)

        if remark:
            instance.remarks.clear()
            remark = Remark.objects.create(order=instance, content=remark)
        if files:
            instance.reports.clear()
            for file in files:
                ReportFile.objects.create(order=instance, file=file)

        return instance.order.sn