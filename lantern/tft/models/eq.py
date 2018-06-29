from django.db import models


class EqKind(models.Model):
    name = models.CharField('装置类别', max_length=3)

    class Meta:
        verbose_name = '装置类别'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Eq(models.Model):
    kind = models.ForeignKey(EqKind, related_name='eqs', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='装置类别')
    name = models.CharField('装置名', max_length=8)

    class Meta:
        verbose_name = '装置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name

class Step(models.Model):
    name = models.CharField('工程站点', max_length=5)
    eq = models.ManyToManyField(Eq, related_name='steps', blank=True, verbose_name='装置')

    class Meta:
        verbose_name = '工程站点'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name
