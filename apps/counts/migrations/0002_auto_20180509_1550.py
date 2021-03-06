# Generated by Django 2.0 on 2018-05-09 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('counts', '0001_initial'),
        ('departs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formcounttotal',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户信息'),
        ),
        migrations.AddField(
            model_name='formcount',
            name='depart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departs.TSDepart', verbose_name='部门信息'),
        ),
        migrations.AddField(
            model_name='formcount',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户信息'),
        ),
    ]
