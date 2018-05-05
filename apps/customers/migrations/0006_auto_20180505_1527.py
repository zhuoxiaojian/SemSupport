# Generated by Django 2.0 on 2018-05-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20180504_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formcustomer',
            name='randid',
            field=models.BigIntegerField(default=959889476, verbose_name='随机数'),
        ),
        migrations.AlterField(
            model_name='seocustomer',
            name='channel',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='来源渠道'),
        ),
        migrations.AlterField(
            model_name='seocustomer',
            name='rand_id',
            field=models.IntegerField(default=228730461, verbose_name='随机数'),
        ),
        migrations.AlterModelTable(
            name='seocustomer',
            table='ys_seo_customer',
        ),
    ]
