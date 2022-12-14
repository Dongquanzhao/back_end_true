# Generated by Django 3.0.8 on 2022-04-13 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20220412_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='goods.GoodsCategory', verbose_name='商品类目')),
                ('goods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goods', to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '首页商品类别广告',
                'verbose_name_plural': '首页商品类别广告',
            },
        ),
    ]
