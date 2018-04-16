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
