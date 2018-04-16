from django.db import models

# Create your models here.
class TSDepart(models.Model):
    departname = models.CharField(max_length=100, verbose_name='部门名称')
    description = models.CharField(max_length=100, verbose_name='部门描述')
    parent = models.ForeignKey('self', verbose_name='上级部门', on_delete=models.CASCADE, null=True, default=None)


    class Meta:
        db_table = 'ys_depart'
        verbose_name = '部门组织'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.departname
