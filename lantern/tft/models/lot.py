from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class LotInfo(models.Model):
    kind = models.CharField('机种', max_length=3)
    size = models.CharField('尺寸', max_length=3)
    height = models.CharField('高度', max_length=5)

class Lot(models.Model):
    info = models.ForeignKey('信息', related_name='lots', on_delete=models.CASCADE)
    name = models.CharField('批次', max_length=8)