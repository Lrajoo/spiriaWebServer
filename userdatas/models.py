from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

class Userdata(models.Model):
    userid = models.CharField(max_length=200)
    age = models.IntegerField()
    spiral = models.ImageField(upload_to='images')
    tremor = models.IntegerField()
    questionnaire = models.IntegerField()
    prediction = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.userid