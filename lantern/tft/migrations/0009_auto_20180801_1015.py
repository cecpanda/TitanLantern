# Generated by Django 2.0.6 on 2018-08-01 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tft', '0008_auto_20180731_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recoverorder',
            old_name='appl',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='recoverorder',
            name='eq',
            field=models.CharField(max_length=50, verbose_name='部分复机设备'),
        ),
    ]
