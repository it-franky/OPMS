from django.db import models

# Create your models here.
MEMBERS = (('1', 'Luffy'), ('2', 'Zoro'), ('3', 'Sanji'), ('4', 'Usopp'), ('5', 'Nami'), ('6', 'Chopper'),
           ('7', 'Robin'), ('8', 'Franky'), ('9', 'Brook'), ('10', 'Jinbe'), ('11', 'Sunny'))


class TodoList(models.Model):  # Table name, has to wrap models.Model to get the functionality of Django.
    big_class = models.CharField(choices=MEMBERS,max_length=10)
    sub_class = models.CharField(max_length=20, null=True)
    tasks = models.CharField(max_length=100, null=True)
    task_list = models.TextField(null=True)
    description = models.CharField(max_length=100,null=True)
    exec_time = models.CharField(max_length=50, null=True)
    exec_place = models.CharField(max_length=50, null=True)
    created_time = models.DateTimeField()
    progress_rate = models.FloatField(default=0)

    def __str__(self):
        return self.tasks
