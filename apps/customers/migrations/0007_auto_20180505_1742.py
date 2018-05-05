# Generated by Django 2.0 on 2018-05-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20180505_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formcustomer',
            name='randid',
            field=models.BigIntegerField(default=1875942163, verbose_name='随机数'),
        ),
        migrations.AlterField(
            model_name='formcustomer',
            name='update_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='最后发现'),
        ),
        migrations.AlterField(
            model_name='seocustomer',
            name='company_name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='公司名称'),
        ),
        migrations.AlterField(
            model_name='seocustomer',
            name='rand_id',
            field=models.IntegerField(default=448169074, verbose_name='随机数'),
        ),
        migrations.AlterField(
            model_name='seocustomer',
            name='update_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='更新时间'),
        ),
    ]
