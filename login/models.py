from django.db import models
from register.models import Country
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    dni = models.CharField(primary_key=True, max_length=10, null=False, blank=False, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, blank=False, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

        
    def __str__(self):
        return self.first_name

    