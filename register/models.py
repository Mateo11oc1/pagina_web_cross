from django.db import models

class Country(models.Model):
    
    code = models.CharField(primary_key=True, max_length=3, null=False, blank=False, unique=True)
    name = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.name


class TypeOfExercise(models.Model):
    
    name = models.CharField(max_length=60, blank=False, null=False)
    description = models.TextField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Exercise(models.Model):
    
    type_of_exercise = models.ForeignKey(TypeOfExercise, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return self.name