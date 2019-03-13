from django.db import models

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

