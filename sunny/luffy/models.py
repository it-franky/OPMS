from django.db import models

# Create your models here.

MEMBERS = (('1', 'Luffy'), ('2', 'Zoro'), ('3', 'Sanji'), ('4', 'Usopp'), ('5', 'Nami'), ('6', 'Chopper'),
           ('7', 'Robin'), ('8', 'Franky'), ('9', 'Brook'), ('10', 'Jinbe'))

# ('11', 'Sunny')


class Members(models.Model):
    name = models.CharField(choices=MEMBERS,max_length=10)
    scope = models.CharField(max_length=100,null=True)

    class Meta:
        verbose_name = "Members"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.scope

# class TheFunctions(models.Model):
#     name = models.ForeignKey(Members,on_delete=models.CASCADE)
#     scope = models.CharField(max_length=100)
#
#     class Meta:
#         verbose_name = "职能"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.scope

class TodoList(models.Model):  # Table name, has to wrap models.Model to get the functionality of Django.
    # name = models.CharField(choices=MEMBERS,max_length=10)
    scope = models.ForeignKey(Members,on_delete=models.CASCADE)
    task = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100,null=True)
    created_time = models.DateTimeField()
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    exec_date = models.IntegerField(default=0)
    progress_rate = models.FloatField(default=0)

    class Meta:
        verbose_name = "TodoList"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task
