# Generated by Django 2.0.7 on 2018-08-07 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tft', '0014_auto_20180806_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortcutcontent',
            name='content',
            field=models.CharField(max_length=50, verbose_name='内容'),
        ),
    ]
