# Generated by Django 2.0 on 2019-05-15 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citys', '0002_auto_20190514_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='地区')),
            ],
            options={
                'verbose_name': '地区列表',
                'verbose_name_plural': '地区列表',
                'db_table': 'ys_area_list',
            },
        ),
        migrations.AddField(
            model_name='province',
            name='area',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='citys.Area', verbose_name='地区'),
        ),
    ]
