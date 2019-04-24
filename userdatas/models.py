from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

class StatusQuerySet(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)
        
class Userdata(models.Model):
    userid = models.CharField(max_length=100)
    age = models.IntegerField()
    spiral = models.ImageField(upload_to='images')
    tremor = models.IntegerField()
    questionnaire = models.IntegerField()
    response1 = models.CharField(max_length=100, default=False)
    response2 = models.CharField(max_length=100, default=False)
    response3 = models.CharField(max_length=100, default=False)
    response4 = models.CharField(max_length=100, default=False)
    response5 = models.CharField(max_length=100, default=False)
    response6 = models.CharField(max_length=100, default=False)
    prediction = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    objects = StatusManager()

    def __str__(self):
        return self.userid

    