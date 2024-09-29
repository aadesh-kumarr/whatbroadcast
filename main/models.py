from django.db import models
import datetime


# from django_countries.fields import Countr1yField

class logdata(models.Model):

    contact=models.CharField(max_length=15,default='none')
    expire=models.DateField(default=None)
    payment=models.CharField(max_length=999,default='none')
    customer_id=models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.contact

  

    
        