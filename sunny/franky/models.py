# _*_ coding:utf-8 _*_
from django.db import models

# Create your models here.


class TestUserMessage(models.Model):
    name = models.CharField(max_length=20,verbose_name="用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100,verbose_name="联系地址")
    message = models.CharField(max_length=500,verbose_name="留言信息")

    class Meta:
        verbose_name = "用户留言信息"


#class TodoList(models.Model):

#    content = models.charF