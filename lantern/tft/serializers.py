from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import Order, StartOrder, ReportFile, Remark, Eq
from account.serializers import UserSerializer


UserModel = get_user_model()


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportFile
        fields = ('file',)


class RemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remark
        fields = ('content',)


class OrderSerializer(serializers.ModelSerializer):
    reports = ReportSerializer(many=True)
    remarks = RemarkSerializer(many=True)
    class Meta:
        model = Order
        fields = ('sn', 'status', 'reports', 'remarks')
        read_only_fields = ('sn', 'status')


class CreateStartOrderSerializer(serializers.Serializer):
    draft = serializers.BooleanField(default=False)
    appl = serializers.HiddenField(default=serializers.CurrentUserDefault())
    eq = serializers.ListField(child=serializers.CharField(min_length=0, max_length=10))
    kind = serializers.CharField(min_length=0, max_length=30)
    step = serializers.CharField(min_length=0, max_length=100)
    found_time = serializers.DateTimeField()
    found_step = serializers.CharField(min_length=0, max_length=10, allow_blank=True)
    
    reason = serializers.CharField(min_length=0, max_length=100)
    users = serializers.ListField(child=serializers.CharField(min_length=0, max_length=128))
    charge_users = serializers.ListField(child=serializers.CharField(min_length=0, max_length=128))
    
    desc = serializers.CharField(min_length=0, max_length=300, allow_blank=True)
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    lot_num = serializers.IntegerField()
    lots = serializers.ListField(child=serializers.CharField(min_length=0, max_length=11))
    condition = serializers.CharField(min_length=0, max_length=200, allow_blank=True)
    deal = serializers.CharField(min_length=0, max_length=100)

    reports = ReportSerializer(many=True)
    remark = serializers.CharField(min_length=0, max_length=300)

    def validate(self, attrs):
        if attrs['start_time'] > attrs['end_time']:
            raise serializers.ValidationError('开始时间超过结束时间')

        return attrs

    def validate_eq(self, value):
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
        # 验证 charge_users
        charge_group = self.get_charge_group()

        for username in value:
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                raise serializers.ValidationError(f'{username} is not existed.')
            if not charge_group.user_set.filter(username=username).exists():
                raise serializers.ValidationError(f'{username} is not a group member.')

        return value

    def get_charge_group(self):
        name_list = self.validated_data['eq']
        name = name_list[0].upper()
        try:
            eq = Eq.objects.get(name=name)
            charge_group = eq.kind.group
        except:
            return None
        return charge_group

    def create(self, validated_data):
        order = Order.objects.create()

        eqs = validated_data.pop('eq')
        step = validated_data.pop('step')
        users = validated_data.pop('users')
        charge_user = validated_data.pop('charge_users')
        remark = validated_data.pop('remark')
        files = validated_data.pop('reports')



        if remark:
            remark = Remark.objects.create(**remark)
        if files:
            for file in files:
                ReportFile.objects.create(order=order, file=file)

        return StartOrder.objects.create(order=order, **validated_data)
