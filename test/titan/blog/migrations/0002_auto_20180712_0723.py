# Generated by Django 2.0.7 on 2018-07-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]