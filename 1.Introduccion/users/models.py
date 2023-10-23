from django.db import models
from django.urls import path, include
import datetime

#  -------------------  CREANDO CAMPOS  -------------------------------

class User(models.Model):
    first_name = models.CharField("el Nombre de la Persona",max_length=30)
    last_name = models.CharField("el Apellido de la Persona",max_length=30)
    cars = models.ManyToManyField('Car', verbose_name="Los carros del usuario")
    
    
STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted')
)


    
class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def was_releasedd_last_week(self):
        if self.release_date < datetime.date(2020,6,6):
            return "Released before last week"
        else:
            return "Released this week"
        
        
    @property
    def get_full_name(self):
        return f"Este es el nombre completo del sitio web: {self.name}"
        
    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return f"/websites/{self.id}"   

    def save(self, *args, **kwargs):
        print("Estamos guardando!")
        super().save(*args, **kwargs)

class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)