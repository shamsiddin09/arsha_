from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi

class Portfolio(models.Model):
    nom = models.CharField(max_length=50)
    tur = models.ForeignKey(Type, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='media')
    data = models.DateField()
class Service(models.Model):
    nm = models.CharField(max_length=50)
    malumot = models.CharField(max_length=50)
class Team(models.Model):
    ismi = models.CharField(max_length=50)
    fam = models.CharField(max_length=50)
    yosh = models.IntegerField()
    rasm = models.ImageField(upload_to='media')
    lavozimi = models.ForeignKey(Type, on_delete=models.CASCADE)
