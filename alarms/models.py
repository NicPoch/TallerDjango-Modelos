from django.db import models
from measurements.models import Measurement
# Create your models here.
class Alarm(models.Model):
    name=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    dateTime=models.DateField(auto_now_add=True)
    measurements=models.ManyToManyField(Measurement)

    def __str__(self):
        return 'Alarm %s (%s)'%(self.name,self.descripcion)