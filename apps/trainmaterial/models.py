from django.db import models
from trainmaterial.validators import validate_file_extension
import datetime
from django.utils.safestring import mark_safe
from SemSupport.settings import PREVIEW_DOMAIN
# Create your models here.
# 销售培训资料
class Trainmaterial(models.Model):
    train_type = models.CharField(max_length=255, verbose_name='培训类型', null=False, blank=False)
    train_file = models.FileField(upload_to='trainFiles/', verbose_name='培训文件', blank=False, null=False, help_text='请选择不大于50M的文档', validators=[validate_file_extension])
    train_remark = models.TextField(verbose_name='备注说明', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.datetime.now)

    class Meta:
        db_table = 'ys_trainmaterial'
        verbose_name = '培训文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.train_type

    def showTrainFile(self):
        return (self.train_file.name).replace("trainFiles/", "")

    showTrainFile.short_description = '文件名'


    def changeTrainFile(self):
        return mark_safe('''<script type='text/javascript'>function openFrame'''+str(self.id)+'''(){window.open("'''+PREVIEW_DOMAIN+self.train_file.url+'''");}</script><a class='btn btn-primary' onclick='openFrame'''+str(self.id)+'''();'>预览</a>''')

    changeTrainFile.short_description = '操作'