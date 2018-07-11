from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    GENDER_CHOICES = (
        ("M", "男"),
        ("F", "女")
    )
    # username
    realname = models.CharField('真名', max_length=10, blank=True, null=True)
    email = models.EmailField(_('邮箱'), max_length=100, blank=True, null=True)
    mobile = models.CharField("手机", max_length=11, blank=True, null=True)
    phone = models.CharField('电话', max_length=6, blank=True, null=True)
    avatar = models.ImageField('头像', upload_to='avatars/%Y/%m', blank=True,
                               null=True, default="avatars/default.png")

    gender = models.CharField("性别", max_length=1, choices=GENDER_CHOICES,
                              default="M")
    birthday = models.DateField("出生年月", blank=True, null=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username


class GroupSetting(models.Model):
    group = models.OneToOneField(Group, related_name='settings', on_delete=models.CASCADE, verbose_name='科室')
    code = models.CharField('代码', max_length=5, unique=True)

    class Meta:
        verbose_name = '科室代码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.group.name
