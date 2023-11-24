from django.db import models
from register.models import Country, Gender
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    dni = models.CharField(
        primary_key=True, 
        max_length=10, 
        null=False, 
        blank=False, 
        unique=True, 
        verbose_name='Cédula de indentidad')
    
    country = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE,
        verbose_name='País')
    
    username = models.CharField(
        max_length=150, 
        unique=True, 
        null=False, 
        blank=False, 
        verbose_name='Nombre de usuario')
    
    first_name = models.CharField(
        max_length=20, 
        null=False,
        blank=False,
        verbose_name='Nombre')
    
    last_name = models.CharField(
        max_length=25, 
        null=True, 
        blank=True,
        verbose_name='Apellido')
    
    email = models.EmailField(
        unique=True,
        null=False, 
        blank=False,
        verbose_name='Email')
    
    phone = models.CharField(
        max_length=10, 
        null=True, 
        blank=True,
        verbose_name='Teléfono')
    
    gender = models.ForeignKey(
        Gender, 
        on_delete=models.CASCADE,
        verbose_name='Género')
    
    
    date_of_birth = models.DateField(
        null=True, 
        blank=True,
        verbose_name='Fecha de nacimiento')
    
    height = models.IntegerField(null=True, blank=True, verbose_name='Estatura')
    
    weight = models.IntegerField(null=True, blank=True, verbose_name='Peso')

        
    def __str__(self):
        return self.first_name

    