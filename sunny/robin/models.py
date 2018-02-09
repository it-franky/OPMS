from django.db import models

# Create your models here.

ReadingType = (('1','纸质书'),('2','电子书'),('3','视频学习'))

class ReadingHistory(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(choices=ReadingType,max_length=2)

    class Meta:
        verbose_name = "已读"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name