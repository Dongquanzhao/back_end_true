# Generated by Django 3.0.8 on 2022-04-14 20:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20220414_1950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderinfo',
            options={'verbose_name': '订单', 'verbose_name_plural': '订单'},
        ),
        migrations.RenameField(
            model_name='orderinfo',
            old_name='pay_script',
            new_name='post_script',
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trade.OrderInfo', verbose_name='订单信息'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_sn',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('success', '成功'), ('cancel', '取消'), ('paying', '待支付')], default='paying', max_length=100, verbose_name='订单状态'),
        ),
    ]
