# Generated by Django 2.0 on 2018-05-09 15:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xs_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='销售姓名')),
                ('hit_url', models.CharField(max_length=255, verbose_name='点击域名')),
                ('hit_count', models.IntegerField(default=0, verbose_name='点击次数')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2018, 5, 9, 15, 50, 35, 732336), verbose_name='点击时间')),
            ],
            options={
                'verbose_name': '点击详情',
                'verbose_name_plural': '点击详情',
                'db_table': 'form_count_details',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='FormCountTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xs_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='销售姓名')),
                ('url_count', models.IntegerField(default=0, verbose_name='URL条数')),
                ('create_time', models.DateField(blank=True, max_length=255, null=True, verbose_name='统计时间')),
                ('depart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departs.TSDepart', verbose_name='部门信息')),
            ],
            options={
                'verbose_name': '域名统计',
                'verbose_name_plural': '域名统计',
                'db_table': 'form_count_total',
                'ordering': ['-create_time'],
            },
        ),
    ]
