from django.db import models

# Create your models here.
class FormRegionCity(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='城市')

    class Meta:
        db_table = 'ys_city'
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='地区')

    class Meta:
        db_table = 'ys_area_list'
        verbose_name = '地区列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='省份')
    area = models.ForeignKey(Area, default=None, null=True, on_delete=models.SET_NULL, verbose_name='所属地区')

    class Meta:
        db_table = 'ys_province_list'
        verbose_name = '省份列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='城市')
    province = models.ForeignKey(Province, verbose_name='所属省份', default=None, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'ys_city_list'
        verbose_name = '城市列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
