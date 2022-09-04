# Generated by Django 3.0.8 on 2022-04-12 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(default=10, max_length=11, verbose_name='电话'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]
