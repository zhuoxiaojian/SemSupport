from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=255, verbose_name="渠道来源", unique=True, null=False, blank=False)

    class Meta:
        db_table = "ys_channel"
        verbose_name = "渠道信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name