from django.db import models
from measurements.models import Measurement
import enum
# Create your models here.
class Alarm(models.Model):
    name=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    dateTime=models.DateField(auto_now_add=True)
    measurements=models.ManyToManyField(Measurement,related_name='alarms')
    
    def __str__(self):
        places=[]
        for s in self.measurements.all():
            places.append(s.place)
        return 'Alarm %s (%s) of: %s'%(self.name,self.descripcion,', '.join(places))
