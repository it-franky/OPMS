import datetime

from django.db import models


# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=10)
    label = models.CharField(default=None,max_length=50, verbose_name="标签")

    class Meta:
        verbose_name = "Members"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class TheFunctions(models.Model):
    name = models.ForeignKey(Members, on_delete=models.CASCADE)
    scope = models.CharField(max_length=100)

    class Meta:
        verbose_name = "职能"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.scope


class TodoList(models.Model):
    # 当下/重要
    important = models.BooleanField(default=False)
    scope = models.ForeignKey(TheFunctions, on_delete=models.CASCADE)
    task = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    created_time = models.DateTimeField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(default=datetime.date(2100, 12, 31))
    progress_rate = models.FloatField(default=0)

    class Meta:
        verbose_name = "TodoList"
        verbose_name_plural = verbose_name
        ordering = ['-important']

    def __str__(self):
        return self.task
