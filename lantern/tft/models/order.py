import os

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from .eq import Eq
from .lot import Lot


UserModel = get_user_model()


def default_order_sn():
    now = timezone.localtime()
    return now.strftime('%y%m%d-%H%M%S-%f')


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
    sn = models.CharField('编号', max_length=25, unique=True, default=default_order_sn)
    status = models.CharField('状态', choices=STATUS_CHOICES, max_length=2, default='0')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sn


def report_handler(instance, filename):
    # instance.id 还未存在
    filename = os.path.split(filename.strip())[-1]
    # name, suffix = os.path.splitext(filename)
    return f"reports/{instance.order.sn}/{filename}"


class ReportFile(models.Model):
    order = models.ForeignKey(Order, related_name='reports', on_delete=models.CASCADE, verbose_name='订单')
    file = models.FileField(upload_to=report_handler, blank=True, null=True, verbose_name='调查报告')

    class Meta:
        verbose_name = '调查报告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.sn


class StartOrder(models.Model):
    order = models.OneToOneField(Order, related_name='startorder', on_delete=models.CASCADE, verbose_name='订单')
    draft = models.BooleanField('草稿箱', default=False)
    appl = models.ForeignKey(UserModel, related_name='startorders', on_delete=models.PROTECT, verbose_name='申请人')
    created = models.DateTimeField('申请时间', auto_now_add=True)

    # department  开单工程  从 appl 中自取
    # charge_group  责任工程  从停机设备中获取

    eq = models.ManyToManyField(Eq, related_name='startorders', verbose_name='停机设备')
    kind = models.CharField('停机机种', max_length=30, blank=True, null=True)
    step = models.CharField('停机站点', max_length=100, blank=True, null=True)
    found_time = models.DateTimeField('发现时间')
    # 做验证，这个站点下是否有停机设备
    found_step = models.CharField('发现站点', max_length=10, blank=True, null=True)
    
    reason = models.TextField('停机原因', max_length=100, blank=True, null=True)
    users = models.ManyToManyField(UserModel, related_name='noticed_startorders', blank=True, verbose_name='通知生产人员')
    # 做验证，必须停机设备的组下的人员
    charge_users = models.ManyToManyField(UserModel, related_name='charged_startorders', blank=True, verbose_name='通知制程人员')
    
    desc = models.TextField('异常描述', max_length=300, blank=True)
    start_time = models.DateTimeField('受害开始时间', blank=True, null=True)
    end_time = models.DateTimeField('受害结束时间', blank=True, null=True)
    lot_num = models.PositiveIntegerField('受害批次数', blank=True, null=True)
    lots = models.ManyToManyField(Lot, related_name="+", blank=True, verbose_name='异常批次')
    condition = models.TextField('复机条件', max_length=200, blank=True)
    deal = models.TextField('处理方法', max_length=100, blank=True, default='停机')


    class Meta:
        verbose_name = '开单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.sn


class StartAudit(models.Model):
    order = models.OneToOneField(Order, related_name='startaudit', on_delete=models.CASCADE, verbose_name='订单')
    
    p_signer = models.ForeignKey(UserModel, related_name='p_startaudit', blank=True, null=True, on_delete=models.PROTECT, verbose_name='生产签停')
    p_time = models.DateTimeField('生产签停时间', blank=True, null=True)
    
    c_signer = models.ForeignKey(UserModel, related_name='c_startaudits', blank=True, null=True, on_delete=models.PROTECT, verbose_name='责任工程签停时间')
    c_time = models.DateTimeField('责任工程签停时间', blank=True, null=True)
    
    recipe_close = models.CharField('Recipe关闭', max_length=10, blank=True, null=True)
    recipe_confirm = models.CharField('Recipe确认关闭', max_length=10, blank=True, null=True)

    rejected = models.BooleanField('拒签', default=False)
    reason = models.TextField('拒签理由', max_length=100, blank=True, null=True)

    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('最近修改', auto_now=True)

    class Meta:
        verbose_name = '开单审核'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.sn


class RecoverOrder(models.Model):
    order = models.ForeignKey(Order, related_name='recoverorders', on_delete=models.CASCADE, verbose_name='订单')
    appl = models.ForeignKey(UserModel, related_name='recoverorders', on_delete=models.PROTECT, verbose_name='申请人')
    created = models.DateTimeField('申请时间', auto_now_add=True)

    partial = models.BooleanField('部分复机', default=False)
    kind = models.CharField('部分复机机种', max_length=10, blank=True, null=True)
    step = models.CharField('部分复机站点', max_length=100, blank=True, null=True)
    reason = models.TextField('部分复机理由', max_length=100, blank=True, null=True)

    solution = models.TextField('责任单位对策说明', max_length=300, blank=True)
    explain = models.TextField('先行lot结果说明', max_length=300, blank=True)

    class Meta:
        verbose_name = '复机申请'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.sn


class RecoverAudit(models.Model):
    recover_order = models.OneToOneField(RecoverOrder, related_name='audit', on_delete=models.CASCADE, verbose_name='复机申请单')

    qc_signer = models.ForeignKey(UserModel, related_name='qc_recoveraudits', blank=True, null=True, on_delete=models.PROTECT, verbose_name='QC签停')
    qc_time = models.DateTimeField('QC签停时间', blank=True, null=True)
    
    p_signer = models.ForeignKey(UserModel, related_name='p_recoveraudit', blank=True, null=True, on_delete=models.PROTECT, verbose_name='生产签停')
    p_time = models.DateTimeField('生产签停时间', blank=True, null=True)
    remark = models.TextField('生产批注', max_length=200, blank=True, null=True)

    rejected = models.BooleanField('拒签', default=False)
    reason = models.TextField('拒签理由', max_length=100, blank=True, null=True)

    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('最近修改', auto_now=True)

    class Meta:
        verbose_name = '复机审核'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.recover_order.order.sn


class Remark(models.Model):
    order = models.ForeignKey(Order, related_name='remarks', on_delete=models.CASCADE, verbose_name='订单')
    content = models.TextField('内容', max_length=300)

    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('最近修改', auto_now=True)

    class Meta:
        ordering = ['-created', '-modified']
        verbose_name = '最新批注'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.sn
