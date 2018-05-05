from django.db import models
from datetime import datetime
from departs.models import TSDepart
# Create your models here.
from users.models import UserProfile
from departs.models import TSDepart
class FormCount(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户信息', null=True, blank=True, on_delete=models.CASCADE)
    depart = models.ForeignKey(TSDepart, verbose_name='部门信息', null=True, blank=True, on_delete=models.CASCADE)
    xs_name = models.CharField(max_length=255, verbose_name='销售姓名', null=True, blank=True)
    hit_url = models.CharField(max_length=255, verbose_name='点击域名')
    hit_count = models.IntegerField(verbose_name='点击次数', default=0)
    create_time = models.DateTimeField(verbose_name='点击时间', default=datetime.now())


    class Meta:
        db_table = 'form_count_details'
        verbose_name = '点击详情'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']


    def __str__(self):
        return self.user.username

class FormCountTotal(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户信息', null=True, blank=True, on_delete=models.CASCADE)
    depart = models.ForeignKey(TSDepart, verbose_name='部门信息', null=True, blank=True, on_delete=models.CASCADE)
    xs_name = models.CharField(max_length=255, verbose_name='销售姓名', null=True, blank=True)
    url_count = models.IntegerField(verbose_name='URL条数', default=0)
    create_time = models.DateField(max_length=255, verbose_name='统计时间', null=True, blank=True)

    class Meta:
        db_table = 'form_count_total'
        verbose_name = '域名统计'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']



    def __str__(self):
        return self.user.username

