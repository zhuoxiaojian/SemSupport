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
            return up.last_name+up.first_name
        else:
            return None
    change_user_id.short_description = '对应销售'

