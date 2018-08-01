from django.db import transaction
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Order, ID, Report, Remark, Audit, RecoverOrder, RecoverAudit
from account.serializers import UserOfGroupSerializer, GroupSerializer


class StartOrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # group
    # charge_group
    # eq = serializers.ListField(label='停机设备', child=serializers.CharField(max_length=8), min_length=1)
    # lots = serializers.ListField(label='异常批次', child=serializers.CharField(max_length=14, min_length=8), required=False)
    # 下面的这两个字段甚至影响了 retrieveserializer 的 foramt=api 的展示，百思不得其解
    charge_group = serializers.IntegerField(label='责任工程')
    reports = serializers.ListField(label='调查报告', child=serializers.FileField(), required=False)
    remark = serializers.CharField(label='生产批注', max_length=500, required=False)

    class Meta:
        model = Order
        fields = ('id', 'status', 'next', 'user',
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

    def validate(self, attrs):
        '''
        如果开单工程是 QC，不良类型必选
        如果没定义 QC，则不验证
        '''
        groups = attrs['user'].groups.all()
        try:
            qc = Group.objects.get(name='QC')
        except:
            return attrs
        if qc in groups:
            if attrs.get('defect_type') is None:
                raise serializers.ValidationError('您在 QC 组下，defect_type 为必选！')
        return attrs

    def get_id(self):
        '''id 生成
        根据开单工程生成 TEA-A01-001
        若开单用户是超级超级管理员或无科室人员，则使用 model 中默认的时间戳
        从 4000 开始
        '''
        group = self.get_group()


        while True:
            id = ID.objects.create().id
            if not Order.objects.filter(id__icontains=id).exists():
                break
        try:
            code = group.settings.code
        except Exception:
            return f'TEA-000-{id}'
        return f'TEA-{code}-{id}'

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

    def get_status(self):
        group = self.get_group()  # 开单工程，可能为空

        # 开单工程为空，当作不是 QC 处理
        if group is None:
            return '1'
        # 开单工程不是 QC
        elif group.name != 'QC':
            return '1'
        elif group.name == 'QC' and self.validated_data.get('defect_type'):
            return '1'  # 和前面的两个 1 有区别
        elif group.name == 'QC' and not self.validated_data.get('defect_type'):
            return '2'
        return '0'

    def create(self, validated_data):
        user = validated_data.get('user')
        status = self.get_status()

        try:
            with transaction.atomic():
                order = Order.objects.create(id=self.get_id(),
                                             status=status,
                                             next= validated_data.get('next'),
                                             user=user,
                                             group=self.get_group(),  # 有可能为空
                                             found_step=validated_data.get('found_step'),
                                             found_time=validated_data.get('found_time'),
                                             charge_group=Group.objects.get(pk=validated_data.get('charge_group')),
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
                # order.charge_group = Group.objects.get(pk=validated_data.get('charge_group'))
                # order.save()

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

        return order

    def update(self, instance, validated_data):
        # try:
        #     audit = instance.startaudit
        #     recover_order = instance.recoverorders
        # except:
        #     pass

        if Audit.objects.filter(order__id=instance.id).exists():
            raise serializers.ValidationError('已经有审核数据，若要修改请联系管理员删除')

        if RecoverOrder.objects.filter(order__id=instance.id).exists():
            raise serializers.ValidationError('已经有复机数据，若要修改请联系管理员删除')

        user = validated_data.get('user')
        status = self.get_status()

        try:
            with transaction.atomic():
                instance.status = status
                next = validated_data.get('next')
                instance.mod_user = user
                instance.found_step = validated_data.get('found_step', instance.found_step)
                instance.found_time = validated_data.get('found_time', instance.found_time)
                # charge_group
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

                # charge_group
                instance.charge_group = Group.objects.get(pk=validated_data.get('charge_group'))
                instance.save()

                # reports
                instance.reports.all().delete()
                reports = validated_data.get('reports')
                if reports:
                    for file in reports:
                        Report.objects.create(order=instance, file=file)
                # remark
                remark = validated_data.get('remark')
                if remark:
                    Remark.objects.create(user=user, order=instance, content=remark)

        except Exception as e:
            raise serializers.ValidationError(f'出现错误{e}，提交数据被回滚。')

        return instance


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('file',)


class RemarkSerializer(serializers.ModelSerializer):
    user = UserOfGroupSerializer()
    class Meta:
        model = Remark
        fields = ('user', 'content', 'created')


class RetrieveStartOrderSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    user = UserOfGroupSerializer()
    group = GroupSerializer()
    mod_user = UserOfGroupSerializer()
    charge_group = GroupSerializer()
    reports = ReportSerializer(many=True)
    remarks = RemarkSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'next', 'user', 'group', 'created',
                  'mod_user', 'modified',
                  'found_step', 'found_time', 'charge_group',
                  'eq', 'kind', 'step', 'reason',
                  'users', 'charge_users',
                  'desc', 'start_time', 'end_time', 'lot_num', 'lots',
                  'condition', 'defect_type',
                  'reports', 'remarks']

    def get_status(self, obj):
        return obj.get_status_display()


class AuditSerializerBak(serializers.ModelSerializer):
    '''
    order 直接传入字符串，validated_data 就可以得到对应的 Order 实例，
    有自动验证 order
    '''
    class Meta:
        model = Audit
        fields = ('order', 'p_signer', 'p_time', 'c_signer', 'c_time',
                  'recipe_close', 'recipe_confirm', 'rejected', 'reason', 'created')
        # read_only_fields = ('order', 'created')

    def validate_order(self, value):
        print(value)


    def create(self, validated_data):
        order = validated_data.get('order')


class ProductAuditSerializer(serializers.Serializer):
    order = serializers.CharField(label='订单编号')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    time = serializers.HiddenField(default=timezone.now)

    recipe_close = serializers.CharField(label='Recipe关闭人员', max_length=10)
    recipe_confirm = serializers.CharField(label='Recipe确认人员', max_length=10)

    remark = serializers.CharField(label='生产批注', max_length=500, required=False)

    next = serializers.CharField(label='下一步', max_length=2, required=False)

    def validate_order(self, value):
        try:
            order = Order.objects.get(id=value)
        except Exception as e:
            raise serializers.ValidationError(f'无效的订单{value}')
        if order.status != '1':
            raise serializers.ValidationError(f'此单当前的状态是{order.get_status_display()}，不是生产签核')
        return order

    def validate_user(self, value):
        # if not value.groups.all().exists():
        #     raise serializers.ValidationError('您没有加入任何科室，不能进行此操作')
        if not value.groups.filter(name='生产科').exists():
            raise serializers.ValidationError('您不是生产科成员，不能进行此操作')
        return value

    # def validate(self, attrs):
    #     order = attrs.get('order')
    #     if order.status != '1':
    #         raise serializers.ValidationError(f'此单当前的状态是{order.get_status_display()}，还不到生产签核的步骤')
    #     if not attrs.get('user').groups.filter(name='生产科').exists():
    #         raise serializers.ValidationError('您不是生产科成员，不能进行此操作')
    #     return attrs

    def get_status(self, order, audit):
        if not order.group:
            if audit.p_signer:
                return '4'
            return '1'
        elif order.group.name != 'QC':
            if audit.p_signer:
                return '4'
            return '1'
        elif order.group.name == 'QC':
            if order.defect_type:
                if not audit.p_signer:
                    return '1'
                if audit.p_signer and not audit.c_signer:
                    return '2'
                if audit.p_signer and audit.c_signer:
                    if audit.rejected:
                        return '3'
                    return '4'
            else:
                if not audit.c_signer:
                    return '2'
                if audit.c_signer and not audit.rejected:
                    if not audit.p_signer:
                        return '1'
                    else:
                        return '4'
                if audit.c_signer and audit.rejected:
                    return '3'
        return '0'

    def create(self, validated_data):
        order = validated_data.get('order')
        user = validated_data.get('user')
        try:
            with transaction.atomic():
                audit, created = Audit.objects.get_or_create(order=order)
                audit.p_signer = user
                audit.p_time = validated_data.get('time')
                audit.recipe_close = validated_data.get('recipe_close')
                audit.recipe_confirm = validated_data.get('recipe_confirm')
                audit.save()

                order.status = self.get_status(order, audit)
                order.next = validated_data.get('next')
                order.save()

                remark = validated_data.get('remark')
                if remark:
                    Remark.objects.create(user=user, order=order, content=remark)

        except Exception as e:
            raise serializers.ValidationError(f'出现错误{e}，提交数据被回滚。')

        # return {'id': order.id, 'status': order.get_status_display()}
        return order


class ChargeAuditSerializer(serializers.Serializer):
    order = serializers.CharField(label='订单编号')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    time = serializers.HiddenField(default=timezone.now)

    rejected = serializers.BooleanField(label='是否拒签', default=False)
    reason = serializers.CharField(label='拒签理由', max_length=100, required=False)

    next = serializers.CharField(label='下一步', max_length=2, required=False)

    def validate_order(self, value):
        try:
            order = Order.objects.get(id=value)
        except Exception as e:
            raise serializers.ValidationError(f'无效的订单{value}')
        if order.status != '2':
            raise serializers.ValidationError(f'此单当前的状态是{order.get_status_display()}，不是责任工程签核')
        return order

    def validate_user(self, value):
        # 放在 validate 中了
        return value

    def validate(self, attrs):
        order = attrs.get('order')
        user = attrs.get('user')

        if order.charge_group is None:
            pass
        else:
            if order.charge_group not in user.groups.all():
                raise serializers.ValidationError('您不属于责任工程的成员，无权进行此操作')

        if attrs.get('rejected'):
            if not attrs.get('reason'):
                raise serializers.ValidationError('拒签就请填写理由')
        return attrs

    def get_status(self, order, audit):
        if not order.group:
            if audit.p_signer:
                return '4'
            return '1'
        elif order.group.name != 'QC':
            if audit.p_signer:
                return '4'
            return '1'
        elif order.group.name == 'QC':
            if order.defect_type:
                if not audit.p_signer:
                    return '1'
                if audit.p_signer and not audit.c_signer:
                    return '2'
                if audit.p_signer and audit.c_signer:
                    if audit.rejected:
                        return '3'
                    return '4'
            else:
                if not audit.c_signer:
                    return '2'
                if audit.c_signer and not audit.rejected:
                    if not audit.p_signer:
                        return '1'
                    else:
                        return '4'
                if audit.c_signer and audit.rejected:
                    return '3'
        return '0'

    def create(self, validated_data):
        order = validated_data.get('order')
        user = validated_data.get('user')
        try:
            with transaction.atomic():
                audit, created = Audit.objects.get_or_create(order=order)
                audit.c_signer = user
                audit.c_time = validated_data.get('time')
                audit.rejected = True if validated_data.get('rejected') else False
                audit.reason = validated_data.get('reason')
                audit.save()

                order.status = self.get_status(order, audit)
                order.next = validated_data.get('next')
                order.save()

        except Exception as e:
            raise serializers.ValidationError(f'出现错误{e}，提交数据被回滚。')

        # return {'id': order.id, 'status': order.get_status_display()}
        return order


class RecoverOrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RecoverOrder
        fields = ('id', 'order', 'user', 'solution', 'explain',
                  'partial', 'eq', 'kind', 'step')

    def get_status(self, recover_order):
        # 应该重写 create 方法，改变 status
        # 最后还是决定放在 view 中了
        order = recover_order.order
        if order.group is None:
            return '6'
        elif order.group.name != 'QC':
            return '6'
        elif order.group.name == 'QC':
            return '5'
        return '0'

    def validate_order(self, order):
        if order.status != '4' or order.status != '7' or order.status != '8':
            raise serializers.ValidationError(f'{order.get_status_display()}不允许复机申请')

    def validate(self, attrs):
        '''
        开单工程为空：
            任何人都可以申请复机
        开单工程是 QC
            责任工程和 QC 可以申请复机
        开单工程不是 QC
        '''
        order = attrs.get('order')
        user = attrs.get('user')
        if not order.group:
            # 谁都可以申请开单
            pass
        elif order.group.name == 'QC':
            if not user.groups.filter(Q(name=order.charge_group.name) | Q(name='QC')).exists():
                raise serializers.ValidationError('开单工程是 QC，只有责任工程和 QC 才能申请复机')
        else:
            if not user.groups.filter(name=order.charge_group.name).exists():
                raise serializers.ValidationError('开单工程不是是 QC，只有责任工程才能申请复机')

        partial = attrs.get('partial', False)
        # 部分复机
        if partial:
            if not attrs.get('eq') or not attrs.get('kind') or not attrs.get('step'):
                raise serializers.ValidationError('部分复机必须填写复机设备、机种、站点')
        # 全部复机
        elif not partial:
            if attrs.get('eq') or attrs.get('kind') or attrs.get('step'):
                raise serializers.ValidationError('全部复机不需要复机设备、机种、站点')

        return attrs


class QcRecoverAuditSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='复机单ID')
    # order = serializers.CharField(label='订单编号')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    time = serializers.HiddenField(default=timezone.now)

    rejected = serializers.BooleanField(label='是否拒签', default=False)
    reason = serializers.CharField(label='拒签理由', max_length=100, required=False)

    def get_status(self, recover_audit):
        if recover_audit.qc_signer and not recover_audit.p_signer:
            if recover_audit.rejected:
                return '7'
            else:
                return '6'
        if recover_audit.p_signer and not recover_audit.partial:
            return '9'
        if recover_audit.p_signer and recover_audit.partial:
            return '8'
        return '0'

    def validate_id(self, value):
        try:
            recover_order = RecoverOrder.objects.get(id=value)
        except Exception as e:
            raise serializers.ValidationError(f'无效的复机单{value}')
        # if order.status != '2':
        #     raise serializers.ValidationError(f'此单当前的状态是{order.get_status_display()}，不是责任工程签核')
        if recover_order.order.status != '5':
            raise serializers.ValidationError(f'此单当前的状态是{recover_order.order.get_status_display()}，不是生产签核')
        return recover_order

    def validate_user(self, value):
        if not value.groups.filter(name='QC').exists():
            raise serializers.ValidationError('您不是 QC 成员，无法进行此操作')
        return value

    def validate(self, attrs):
        if attrs.get('rejected'):
            if not attrs.get('reason'):
                return serializers.ValidationError('拒签要有理由')
        return attrs

    def create(self, validated_data):
        recover_order = validated_data.get('id')
        user = validated_data.get('user')
        try:
            with transaction.atomic():
                recover_audit, created = RecoverAudit.objects.get_or_create(recover_order=recover_order)
                recover_audit.qc_signer = user
                recover_audit.qc_time = validated_data.get('time')
                recover_audit.rejected = True if validated_data.get('rejected') else False
                recover_audit.save()
        except Exception as e:
            raise serializers.ValidationError(f'出现错误{e}，提交数据被回滚。')

        return recover_audit


class ProductRecoverAuditSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='复机单ID')
    # order = serializers.CharField(label='订单编号')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    time = serializers.HiddenField(default=timezone.now)

    def get_status(self, recover_audit):
        if recover_audit.qc_signer and not recover_audit.p_signer:
            if recover_audit.rejected:
                return '7'
            else:
                return '6'
        if recover_audit.p_signer and not recover_audit.partial:
            return '9'
        if recover_audit.p_signer and recover_audit.partial:
            return '8'
        return '0'

    def validate_id(self, value):
        try:
            recover_order = RecoverOrder.objects.get(id=value)
        except Exception as e:
            raise serializers.ValidationError(f'无效的复机单{value}')
        if recover_order.order.status != '6':
            raise serializers.ValidationError(f'此单当前的状态是{recover_order.order.get_status_display()}，不是QC签核')
        return recover_order

    def validate_user(self, value):
        if not value.groups.filter(name='生产科').exists():
            raise serializers.ValidationError('您不是生产科成员，无法进行此操作')
        return value

    def create(self, validated_data):
        recover_order = validated_data.get('id')
        user = validated_data.get('user')
        try:
            with transaction.atomic():
                recover_audit, created = RecoverAudit.objects.get_or_create(recover_order=recover_order)
                recover_audit.p_signer = user
                recover_audit.p_time = validated_data.get('time')
                recover_audit.save()
        except Exception as e:
            raise serializers.ValidationError(f'出现错误{e}，提交数据被回滚。')

        return recover_audit
