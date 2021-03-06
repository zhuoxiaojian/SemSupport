# Generated by Django 2.0 on 2018-07-17 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='音频标题')),
                ('keyword', models.TextField(blank=True, null=True, verbose_name='关键词')),
                ('abstarct', models.TextField(blank=True, null=True, verbose_name='音频摘要')),
                ('visitType', models.CharField(choices=[('开场白', '开场白'), ('激发兴趣', '激发兴趣'), ('挖掘需求', '挖掘需求'), ('介绍产品', '介绍产品'), ('邀约见面', '邀约见面'), ('二次跟进', '二次跟进'), ('逼单', '逼单'), ('判单', '判单')], db_index=True, max_length=255, verbose_name='访问类型')),
                ('visitResult', models.TextField(blank=True, null=True, verbose_name='访问结果')),
                ('anInterviewCompany', models.CharField(blank=True, max_length=255, null=True, verbose_name='被访公司')),
                ('anInterviewPeople', models.TextField(blank=True, null=True, verbose_name='被访公司参与人员')),
                ('partakeSale', models.TextField(blank=True, null=True, verbose_name='我司参与销售')),
                ('audioFile', models.FileField(upload_to='audioFiles/', verbose_name='音频文件', help_text='请选择mp3文件')),
                ('createTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '音频管理',
                'verbose_name_plural': '音频管理',
                'db_table': 'ys_audio',
            },
        ),
    ]
