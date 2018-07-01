from django.db import models
from django.contrib.auth import get_user_model


# UserModel = get_user_model()

# class LotSize(models.Model):
#     name = models.CharField('尺寸', max_length=4)

#     class Meta:
#         verbose_name = '机种尺寸'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.name


# class LotHeight(models.Model):
#     name = models.CharField('高度', max_length=5)

#     class Meta:
#         verbose_name = '机种高度'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.name


class LotInfo(models.Model):
    kind = models.CharField('机种', max_length=3)
    size = models.CharField('大小', max_length=3)
    height = models.CharField('高度', max_length=4)
    
    class Meta:
        verbose_name = '机种信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.kind


class Lot(models.Model):
    info = models.ForeignKey(LotInfo, verbose_name='机种信息', related_name='lots', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField('批次', blank=True, null=True, max_length=8)

    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '批次'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}'
