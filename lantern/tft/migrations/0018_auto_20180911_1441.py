# Generated by Django 2.0.7 on 2018-09-11 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tft', '0017_auto_20180904_0951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audit',
            options={'ordering': ('-created',), 'verbose_name': '停机签核', 'verbose_name_plural': '停机签核'},
        ),
        migrations.AlterModelOptions(
            name='recoverorder',
            options={'ordering': ('-created',), 'verbose_name': '复机单', 'verbose_name_plural': '复机单'},
        ),
    ]