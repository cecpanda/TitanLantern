# Generated by Django 2.0.6 on 2018-07-25 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tft', '0003_auto_20180725_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='节点名')),
            ],
        ),
        migrations.AddField(
            model_name='flow',
            name='next_node',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tft.Node', verbose_name='下一节点'),
        ),
        migrations.AddField(
            model_name='flow',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='workflow', to='tft.Order', verbose_name='订单'),
        ),
        migrations.AddField(
            model_name='flow',
            name='pre_node',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tft.Node', verbose_name='上一节点'),
        ),
    ]
