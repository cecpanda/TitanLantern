# Generated by Django 2.0.7 on 2018-08-30 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tft', '0015_auto_20180807_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='startorders', to='auth.Group', verbose_name='开单工程'),
            preserve_default=False,
        ),
    ]