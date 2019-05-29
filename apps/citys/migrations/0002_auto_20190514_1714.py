# Generated by Django 2.0 on 2019-05-14 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='城市')),
            ],
            options={
                'verbose_name': '城市列表',
                'verbose_name_plural': '城市列表',
                'db_table': 'ys_city_list',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='省份')),
            ],
            options={
                'verbose_name': '省份列表',
                'verbose_name_plural': '省份列表',
                'db_table': 'ys_province_list',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='citys.Province', verbose_name='所属省份'),
        ),
    ]