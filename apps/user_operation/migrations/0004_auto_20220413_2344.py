# Generated by Django 3.0.8 on 2022-04-13 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0003_auto_20220413_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userleavingmessage',
            name='file',
            field=models.FileField(help_text='上传的文件', upload_to='message/images/', verbose_name='上传的文件'),
        ),
    ]
