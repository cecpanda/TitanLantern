# Generated by Django 2.0.6 on 2018-08-01 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tft', '0009_auto_20180801_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recoverorder',
            name='eq',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='部分复机设备'),
        ),
    ]