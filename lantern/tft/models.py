from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Lot(models.Model):
    kind = models.CharField('机种', max_length=3)
    num = models.CharField('批次号', max_length=8)

    created = models.DateTimeField('添加时间', auto_now_add=True)
    # applicant = models.ForeignKey(UserModel, related_name='applied_lots', on_delete=models.CASCADE)
    # verifier = models.ForeignKey(UserModel, related_name='verified_lots', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'lot'
        verbose_name_plural = 'lots'
        unique_together = (('kind', 'num'))

    def __str__(self):
        return self.kind + self.num


class HoldLot(models.Model):
    STATUS_CHOICES = (
        ('un', '未处理'),
        ('applying', '申请中'),
        ('verified', '已审核')
    )

    lot = models.OneToOneField(Lot, related_name='hold_lot', on_delete=models.CASCADE)
    status = models.CharField('状态', choices=STATUS_CHOICES, default='un', max_length=8)

    applicant = models.ForeignKey(UserModel, 
                                  related_name='applied_lots', 
                                  on_delete=models.CASCADE)
    verifier = models.ForeignKey(UserModel, 
                                 related_name='verified_lots', 
                                 blank=True, 
                                 null=True, 
                                 on_delete=models.CASCADE)
    created = models.DateTimeField('添加时间', auto_now_add=True)
    modified = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = 'holdlot'
        verbose_name_plural = 'holdlots'

    def __str__(self):
        return self.lot.kind + self.lot.num
