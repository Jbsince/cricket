from django.db import models
from django.utils import timezone


# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    dob=models.DateField()
    role=models.CharField(max_length=250)
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name