from django.db import models
from datetime import datetime
# Create your models here.
class Speechcraft(models.Model):
    label = (('开场白', u'开场白'), ('激发兴趣', u'激发兴趣'), ('挖掘需求', u'挖掘需求'), ('导入产品', u'导入产品'), ('邀约见面', u'邀约见面'), ('疑难解答', u'疑难解答'), ('知识普及', u'知识普及'))
    speechLabel = models.CharField(max_length=255, verbose_name='话术对应类型', null=False, blank=False, choices=label)
    speechTarget = models.CharField(max_length=255, verbose_name='话术适用对象', null=True, blank=True)
    speechTitle = models.CharField(max_length=255, verbose_name='话术对应标题', null=True, blank=True)
    speechKeyword = models.CharField(max_length=255, verbose_name='话术对应关键词', null=True, blank=True)
    speechQuestion = models.CharField(max_length=255, verbose_name='话术对应问题', null=True, blank=True)
    speechGoal = models.TextField(verbose_name='话术对应目的', null=True, blank=True)
    speechFlow = models.TextField(verbose_name='话术对应流程', null=True, blank=True)
    speechAnswer = models.TextField(verbose_name='话术对应内容', null=True, blank=True)
    speechRemark = models.TextField(verbose_name='话术对应备注', null=True, blank=True)
    speechCount = models.IntegerField(verbose_name='话术查看次数', default=0)
    speechCreateTime = models.DateTimeField(verbose_name='话术创建时间', default=datetime.now)
    speechUpdateTime = models.DateTimeField(verbose_name='话术更新时间', default=None, null=True, blank=True)



    class Meta:
        db_table = 'ys_speechcraft'
        verbose_name = '话术管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.speechLabel is not None:
            return self.speechLabel

#话术查看
class SpeechcraftShow(Speechcraft):
    class Meta:
        verbose_name = '话术查看'
        verbose_name_plural = verbose_name
        proxy = True

    def __str__(self):
        return self.speechLabel

