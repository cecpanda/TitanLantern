# Generated by Django 2.0.6 on 2018-07-25 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tft', '0002_order_mod_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit',
            name='recipe_close',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Recipe关闭人员'),
        ),
        migrations.AlterField(
            model_name='audit',
            name='recipe_confirm',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Recipe确认人员'),
        ),
    ]
