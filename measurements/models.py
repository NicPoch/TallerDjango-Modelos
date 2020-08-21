from django.db import models
from variables.models import Variable

# Create your models here.
class Measurement(models.Model):
    variable=models.ForeignKey(Variable, on_delete=models.CASCADE)
    value=models.FloatField(null=True,blank=True,default=None)
    unit=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    dateTime=models.DateField(auto_now_add=True)    

    def __str__(self):
        names=[]
        for s in self.alarms.all():
            names.append(s.name)
        return '%s %s %s %s, Alarms(%s)'%(self.variable,self.place,self.value,self.unit,', '.join(names))