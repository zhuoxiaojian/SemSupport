from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
from users.models import UserProfile
class customerUser(models.Model):
    user_id = models.IntegerField(verbose_name='用户id')
    customer_id = models.IntegerField(verbose_name='任务id')
    create_time = models.CharField(max_length=255, verbose_name='分配时间')

    class Meta:
        db_table = 'ys_sale_customer'
        verbose_name = '任务库表'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return str(self.user_id)

    def change_user_id(self):
        up = UserProfile.objects.get(id=self.user_id)
        if up:
            return up.username
        else:
            return None
    change_user_id.short_description = '对应销售'


class BackUpWork(models.Model):
    user_id = models.IntegerField(verbose_name='用户id')
    user_name = models.CharField(verbose_name='用户名', max_length=255, db_index=True)
    sql_str = models.TextField(verbose_name='任务SQL')
    create_time = models.CharField(max_length=255, verbose_name='时间')
    update_time = models.DateTimeField(verbose_name='更新时间', default=None)

    class Meta:
        db_table = 'ys_backup_work'
        verbose_name = '任务备份'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return str(self.user_id)



class BackUpWorkRepeat(BackUpWork):

    class Meta:
        verbose_name = '查看重复'
        verbose_name_plural = verbose_name
        proxy = True
        ordering = ['-create_time']

    def __str__(self):
        return str(self.user_id)


    def repeat_count(self):
        from utils.DateFormatUtil import get_yesterday, get_today
        from customers.models import FormCustomer
        yesB = BackUpWork.objects.filter(create_time=str(get_yesterday()), user_id=self.user_id)
        toB = BackUpWork.objects.filter(create_time=str(get_today()), user_id=self.user_id)
        if yesB.exists() and toB.exists():
            y = yesB[0]
            t = toB[0]
            yy = FormCustomer.objects.raw(y.sql_str)
            tt = FormCustomer.objects.raw(t.sql_str)
            list_company = []
            for y in yy:
                list_company.append(y.company_name)
            for t in tt:
                list_company.append(t.company_name)
            set_company = set(list_company)
            repeat_count = len(list_company) - len(set_company)
            return repeat_count
        return 0
    repeat_count.short_description = '重复总数'