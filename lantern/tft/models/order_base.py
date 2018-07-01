from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .eq import Eq, Step
from .lot import LotInfo, Lot


UserModel = get_user_model()


def default_order_sn():
    now = timezone.localtime()
    return now.strftime('%Y-%m-%d-%H-%M-%S-%f')



class Order(models.Model):
    STATUS_CHOICES = (
        ('0', '未知')
    )
    sn = models.CharField('订单编号', max_length=50, unique=True, default=default_order_sn)
    status = models.CharField('当前状态', max_length=5, default='0')

    class Meta:
        verbose_name = '订单主数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sn


class OpenOrder(models.Model):
    order = models.OneToOneField(Order, related_name='open_order', on_delete=models.PROTECT, verbose_name='开单')
    open_order_user = models.ForeignKey(UserModel, related_name='open_orders', on_delete=models.PROTECT, verbose_name='申请人')
    open_order_department = models.ManyToManyField(Group, related_name='open_orders', blank=True, verbose_name='开单部门')
    open_order_department_responsible = models.ManyToManyField(Group, related_name='open_orders_r', blank=True, verbose_name='责任部门')

    found_step = models.ForeignKey(Step, related_name='orders_find', on_delete=models.PROTECT, verbose_name='发现站点')
    found_time = models.DateTimeField('发现时间')

    eq = models.ManyToManyField(Eq, related_name='open_orders', verbose_name='停机设备')
    kind = models.CharField('停机机种', max_length=5)
    step = models.ManyToManyField(Step, related_name='open_orders', blank=True, verbose_name='停机站点')

    reason = models.CharField('停机原因', max_length=30)

    notice_product_user = models.ManyToManyField(UserModel, related_name='+', blank=True, verbose_name='通知生产人员')
    unotice_process_user = models.ManyToManyField(UserModel, related_name='+', blank=True, verbose_name='通知制程人员')

    desc = models.TextField('异常描述', max_length=200)
    start_time = models.DateTimeField('受害开始时间', blank=True, null=True)
    end_time = models.DateTimeField('受害结束时间', blank=True, null=True)

    report = models.FileField(upload_to='reports/%Y/%m/%d/', blank=True, null=True, verbose_name='调查报告')

    lot_num = models.PositiveSmallIntegerField('受害批次数')
    lots = models.ManyToManyField(Lot, related_name="+", blank=True, verbose_name='异常批次')

    recover_condition = models.TextField('复机条件', max_length=200)

    created= models.DateTimeField('开单时间', auto_now_add=True)
    modified = models.DateTimeField('最近更新', auto_now=True)

    class Meta:
        verbose_name = '停机单'
        verbose_name_plural = verbose_name


class OpenOederSign(models.Model):
    ## 审核
    order = models.OneToOneField(Order, related_name='open_order_sign', on_delete=models.PROTECT, verbose_name='审核单')

    product_leader = models.ForeignKey(UserModel, related_name='+', blank=True, null=True, on_delete=models.PROTECT, verbose_name='生产领班签停')
    product_leader_time = models.DateTimeField('生产签停时间', auto_now_add=True)

    related_user = models.ForeignKey(UserModel, related_name='+', blank=True, null=True, on_delete=models.PROTECT, verbose_name='责任工程签停')
    related_user_time = models.DateTimeField('责任工程签停时间', auto_now_add=True)

    recipe_close = models.ForeignKey(UserModel, related_name='+', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Recipe 关闭人员')
    recipe_close_confirm = models.ForeignKey(UserModel, related_name='+', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Recipe 确认人员')

    is_rejected = models.BooleanField('是否拒签', default=False)
    reason_rejected = models.TextField('拒签理由')
    
    created= models.DateTimeField('审核时间', auto_now_add=True)
    modified = models.DateTimeField('最近更新', auto_now=True)

    class Meta:
        verbose_name = '审核停机单'
        verbose_name_plural = verbose_name



class RecoverOrder(models.Model):
    order = models.OneToOneField(Order, related_name='recover_order', on_delete=models.PROTECT, verbose_name='开单')

    solution = models.TextField('责任单位对策说明')
    pre_lot_solution = models.TextField('先行批次结果说明')

    apply_user = models.ForeignKey(UserModel, related_name='apply_recover_orders', blank=True, null=True, on_delete=models.PROTECT)
    apply_time = models.DateTimeField('复机签复时间')

    qc_user = models.ForeignKey(UserModel, related_name='qc_recover_orders', blank=True, null=True, on_delete=models.PROTECT)
    qc_time = models.DateTimeField('品质签复时间')

    product_user = models.ForeignKey(UserModel, related_name='product_recover_orders', blank=True, null=True, on_delete=models.PROTECT)
    product_time = models.DateTimeField('生产签复时间')


    class Meta:
        verbose_name = '复机单'
        verbose_name_plural = verbose_name
