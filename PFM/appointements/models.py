
# Create your models here.
from django.db import models
from shortuuid.django_fields import ShortUUIDField

class Appoi(models.Model):
    aid = ShortUUIDField(unique=True, length=10)
    NomClient = models.CharField(max_length=100)
    EmailC = models.EmailField(max_length=100)      
    TypeMar = models.CharField(max_length=100)
    Comment = models.CharField(max_length=250)
    dateApp = models.DateField()

    class Meta:
        verbose_name_plural = "Appointments"

    def __str__(self):
        return self.NomClient  


 

