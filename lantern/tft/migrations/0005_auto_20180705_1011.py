# Generated by Django 2.0.6 on 2018-07-05 02:11

from django.db import migrations, models
import tft.models.order


class Migration(migrations.Migration):

    dependencies = [
        ('tft', '0004_auto_20180704_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='eq',
        ),
        migrations.RemoveField(
            model_name='lot',
            name='modified',
        ),
        migrations.AlterField(
            model_name='order',
            name='sn',
            field=models.CharField(default=tft.models.order.default_order_sn, max_length=25, unique=True, verbose_name='编号'),
        ),
        migrations.RemoveField(
            model_name='recoverorder',
            name='step',
        ),
        migrations.AddField(
            model_name='recoverorder',
            name='step',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='部分复机站点'),
        ),
        migrations.AlterField(
            model_name='startorder',
            name='found_step',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='发现站点'),
        ),
        migrations.AlterField(
            model_name='startorder',
            name='kind',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='停机机种'),
        ),
        migrations.RemoveField(
            model_name='startorder',
            name='step',
        ),
        migrations.AddField(
            model_name='startorder',
            name='step',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='停机站点'),
        ),
        migrations.DeleteModel(
            name='Step',
        ),
    ]