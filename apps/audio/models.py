from django.db import models

# Create your models here.
import datetime
from django.utils.safestring import mark_safe
from audio.validators import validate_file_extension
class Audio(models.Model):
    labelDist = (('开场白', u'开场白'), ('激发兴趣', u'激发兴趣'), ('挖掘需求', u'挖掘需求'), ('介绍产品', u'介绍产品'), ('邀约见面', u'邀约见面'), ('二次跟进', u'二次跟进'), ('逼单', u'逼单'), ('判单', u'判单'))
    visitType = models.CharField(max_length=255, verbose_name='访问类型', blank=False, null=False, db_index=True, choices=labelDist)
    title = models.CharField(max_length=255, verbose_name='音频标题', blank=True, null=True)
    keyword = models.TextField(verbose_name='关键词', blank=True, null=True)
    abstarct = models.TextField(verbose_name='音频摘要', blank=True, null=True)
    visitResult = models.TextField(verbose_name='访问结果', blank=True, null=True)
    anInterviewCompany = models.CharField(max_length=255, verbose_name='被访公司', blank=True, null=True)
    anInterviewPeople = models.TextField(verbose_name='被访公司参与人员', blank=True, null=True)
    partakeSale = models.TextField(verbose_name='我司参与销售', blank=True, null=True)
    audioFile = models.FileField(upload_to='audioFiles/', verbose_name='音频文件', blank=False, null=False, help_text='请选择不大于5M的mp3文件', validators=[validate_file_extension])
    createTime = models.DateTimeField(verbose_name='创建时间', default=datetime.datetime.now)

    class Meta:
        db_table = 'ys_audio'
        verbose_name = '音频管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.visitType

    def changeAudioFile(self):
        # auto - 当页面加载后载入整个音频
        # meta - 当页面加载后只载入元数据
        # none - 当页面加载后不载入音频
        # controlsList="nodownload" 屏蔽上传按钮
        s = '<audio controls="controls" preload="none"><source src="/media/'+str(self.audioFile)+'" type="audio/mpeg"></audio>'
        return mark_safe(s)
    changeAudioFile.short_description = '播放'

