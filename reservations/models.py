from django.db import models
from django.forms import CharField

# Create your models here.
class Reservations(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=25)
    number = models.IntegerField()
    date = models.DateField(auto_now=False , auto_now_add=False)
    time = models.TimeField(auto_now=False , auto_now_add=False)
    
    def __str__(self):
        return self.name