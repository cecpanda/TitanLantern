# Generated by Django 2.0.6 on 2018-07-04 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tft', '0003_auto_20180704_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recoveraudit',
            name='p_signer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='p_recoveraudit', to=settings.AUTH_USER_MODEL, verbose_name='生产签停'),
        ),
        migrations.AlterField(
            model_name='recoveraudit',
            name='p_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='生产签停时间'),
        ),
        migrations.AlterField(
            model_name='recoveraudit',
            name='qc_signer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='qc_recoveraudits', to=settings.AUTH_USER_MODEL, verbose_name='QC签停'),
        ),
        migrations.AlterField(
            model_name='recoveraudit',
            name='qc_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='QC签停时间'),
        ),
        migrations.AlterField(
            model_name='recoveraudit',
            name='rejected',
            field=models.BooleanField(default=False, verbose_name='拒签'),
        ),
        migrations.AlterField(
            model_name='recoverorder',
            name='kind',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='部分复机机种'),
        ),
        migrations.AlterField(
            model_name='reportfile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='startaudit',
            name='c_signer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='c_startaudits', to=settings.AUTH_USER_MODEL, verbose_name='责任工程签停时间'),
        ),
        migrations.AlterField(
            model_name='startaudit',
            name='c_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='责任工程签停时间'),
        ),
        migrations.AlterField(
            model_name='startaudit',
            name='p_signer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='p_startaudit', to=settings.AUTH_USER_MODEL, verbose_name='生产签停'),
        ),
        migrations.AlterField(
            model_name='startaudit',
            name='p_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='生产签停时间'),
        ),
        migrations.AlterField(
            model_name='startaudit',
            name='rejected',
            field=models.BooleanField(default=False, verbose_name='拒签'),
        ),
        migrations.AlterField(
            model_name='startorder',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='草稿箱'),
        ),
        migrations.AlterField(
            model_name='startorder',
            name='reason',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='停机原因'),
        ),
    ]
