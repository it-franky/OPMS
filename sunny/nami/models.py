from django.db import models

# Create your models here.

PASSWORD_TYPE = (('1', 'APP'), ('2', '网站'), ('3', '银行卡'), ('4', '信用卡'), ('5', '运维'))

class Passwd(models.Model):
    title = models.CharField(choices=PASSWORD_TYPE,max_length=2,default='1')
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    website = models.CharField(max_length=40,null=True,blank=True)
    mark = models.CharField(max_length=100)

    class Meta:
        verbose_name = "密码"
        verbose_name_plural = verbose_name