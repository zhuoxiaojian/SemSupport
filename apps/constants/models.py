from django.db import models

# Create your models here.
class Constants(models.Model):
    key = models.CharField(max_length=255, verbose_name='参数名', unique=True, null=False, blank=False)
    value = models.CharField(max_length=255, verbose_name='参数值', null=True, blank=True)
    remark = models.CharField(max_length=255, verbose_name='备注', null=True, blank=True)

    class Meta:
        db_table = 'ys_constants'
        verbose_name = '参数信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.key

