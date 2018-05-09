from django.db import models

# Create your models here.
from customers.models import FormCustomer
from datetime import datetime
class addUpByDepart(FormCustomer):
    # depart = models.CharField(max_length=255, verbose_name='销售部门')
    # total_amount = models.IntegerField(verbose_name='签单金额')
    # total_business = models.IntegerField(verbose_name='商机')
    # total_amountNum = models.IntegerField(verbose_name='签单数量')
    # create_time = models.DateTimeField(verbose_name='时间', default=datetime.now())

    class Meta:
        verbose_name = '部门销售统计'
        verbose_name_plural = verbose_name
        proxy = True


    def __str__(self):
        return self.depart

class CountBySale(models.Model):
    sale = models.CharField(max_length=255, verbose_name='销售人员')
    total_amount = models.IntegerField(verbose_name='签单金额')
    total_business = models.IntegerField(verbose_name='商机')
    total_amountNum = models.IntegerField(verbose_name='签单数量')
    create_time = models.DateTimeField(verbose_name='统计时间')

    class Meta:
        db_table = 'ys_count_by_sale'
        verbose_name = '销售人员统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sale

class CountByDepart(models.Model):
    depart = models.CharField(max_length=255, verbose_name='销售部门')
    total_amount = models.IntegerField(verbose_name='签单金额')
    total_business = models.IntegerField(verbose_name='商机')
    total_amountNum = models.IntegerField(verbose_name='签单数量')
    create_time = models.DateTimeField(verbose_name='统计时间')

    class Meta:
        db_table = 'ys_count_by_depart'
        verbose_name = '销售部门统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.depart







