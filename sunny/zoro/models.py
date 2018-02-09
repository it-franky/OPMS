from django.db import models


# Create your models here.


class Fitness(models.Model):
    project = models.CharField(max_length=50)
    load = models.FloatField(default=0)
    count = models.IntegerField(default=12)
    groups = models.IntegerField(default=4)
    place = models.CharField(choices=(("gym", "健身房"), ("home", "在家"), ("outdoor", "户外")), max_length=10, default="gym")

    class Meta:
        verbose_name = "健身"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.project


class FitnessRecords(models.Model):
    exec_date = models.DateField()
    content = models.TextField(max_length=100)
    # place = models.CharField(choices=(("gym","健身房"),("home","在家"),("outdoor","户外")),max_length=10,default="gym")
    photo = models.ImageField(upload_to="courses/%Y/%m", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "健身记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.exec_date.strftime("%Y%m%d")


class Cycling(models.Model):
    riding_date = models.DateField()
    distance = models.FloatField()
    duration = models.IntegerField()
    route = models.ImageField(upload_to="zoro/cycling/")

    class Meta:
        verbose_name = "骑行"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.riding_date.strftime("%Y%m%d")


class Journey(models.Model):
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    spend = models.FloatField(default=0)

    class Meta:
        verbose_name = "旅行"
        verbose_name_plural = verbose_name
