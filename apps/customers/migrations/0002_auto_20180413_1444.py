# Generated by Django 2.0 on 2018-04-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formcustomer',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='所在城市'),
        ),
        migrations.AlterField(
            model_name='formcustomer',
            name='randid',
            field=models.BigIntegerField(default=2095909273, verbose_name='随机数'),
        ),
        migrations.AlterField(
            model_name='seocustomer',
            name='rand_id',
            field=models.IntegerField(default=968640785, verbose_name='随机数'),
        ),
    ]
