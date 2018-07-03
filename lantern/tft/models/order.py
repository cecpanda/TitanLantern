import os

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
        ('0', '未知'),
        ('1', '待审核'),
        ('2', '停机拒签'),
        ('3', '停机完成'),
        ('4', '待 QC 签核复机'),
        ('5', '驳回复机申请'),
        ('6', '待生产签核'),
        ('7', '完成部分复机'),
        ('8', '完成复机')
    )
    sn = models.CharField('编号', max_length=50, unique=True, default=default_order_sn)
    status = models.CharField('状态', choices=STATUS_CHOICES, max_length=2, default='0')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name


def report_handler(instance, filename):
    filename = filename.strip()
    name = os.path.split(filename)
    suffix = os.path.splitext(filename)
    return f"{instance.order.sn}/{instance.order.sn}-{instance.id}{suffix}"


class ReportFile(models.Model):
    order = models.ForeignKey(Order, related_name='reports', on_delete=models.CASCADE, verbose_name='订单')
    file = models.FileField(upload_to=report_handler, blank=True, null=True, verbose_name='调查报告')

    class Meta:
        verbose_name = '调查报告'
        verbose_name_plural = verbose_name


class StartOrder(models.Model):
    order = models.OneToOneField(Order, related_name='startorder', on_delete=models.CASCADE, verbose_name='订单')
    draft = models.BooleanField('放入草稿箱', default=False)
    applicant = models.ForeignKey(UserModel, related_name='startorders', on_delete=models.PROTECT, verbose_name='申请人')
    # department，从 user 中自取
    created = models.DateTimeField('申请时间', auto_now_add=True)
    # charge_group 从停机设备中获取
    # charge_group = models.ManyToManyField(Group, related_name='startorders', blank=True, verbose_name='开单部门')
    eq = models.ManyToManyField(Eq, related_name='startorders', verbose_name='停机设备')
    kind = models.CharField('停机机种', max_length=5)
    found_time = models.DateTimeField('发现时间')
    found_step = models.CharField('发现站点', max_length=10)
    # 做验证，这个站点下是否有停机设备
    step = models.ManyToManyField(Step, related_name='startorders', blank=True, verbose_name='停机站点')
    reason = models.TextField('停机原因', max_length=110)
    users = models.ManyToManyField(UserModel, related_name='+', blank=True, verbose_name='通知生产人员')
    # 做验证，必须停机设备的组下的人员
    charge_users = models.ManyToManyField(UserModel, related_name='+', blank=True, verbose_name='通知制程人员')
    desc = models.TextField('异常描述', max_length=320)
    start_time = models.DateTimeField('受害开始时间', blank=True, null=True)
    end_time = models.DateTimeField('受害结束时间', blank=True, null=True)
    lot_num = models.PositiveIntegerField('受害批次数')
    lots = models.ManyToManyField(Lot, related_name="+", blank=True, verbose_name='异常批次')
    condition = models.TextField('复机条件', max_length=200)
    deal = models.CharField('处理方法', max_length=25, blank=True, default='停机')




