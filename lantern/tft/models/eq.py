from django.db import models


class EqKind(models.Model):
    name = models.CharField('装置类别', max_length=3)
    created = models.DateTimeField('添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '装置类别'

    def __str__(self):
        return self.name

class Eq(models.Model):
    kind = models.ForeignKey(EqKind, related_name='eqs', balank=True, null=True, on_delete=models.SET_NULL, verbose_name='装置')
    name = models.CharField('装置名', max_length=8)

    class Meta:
        verbose_name = '装置'

    def __str__(self):
        return  self.name

class EqStep(models.Model):
    step = models.IntegerField('站点')
    eq = models.ManyToManyField(Eq, related_name='steps', balank=True, null=True, on_delete=models.SET_NULL, verbose_name='装置')
