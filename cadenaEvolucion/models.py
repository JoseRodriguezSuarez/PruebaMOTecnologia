from django.db import models


# Create your models here.
class Pokemon(models.Model):
    nPok=models.IntegerField()
    nombre=models.CharField(max_length=100)
    peso=models.IntegerField()
    altura=models.IntegerField()
    cadEvolutiva=models.IntegerField()
    hp=models.IntegerField()
    attack=models.IntegerField()
    defense=models.IntegerField()
    special_attack=models.IntegerField()
    special_defense=models.IntegerField()
    speed=models.IntegerField()
    nivelEvolutivo=models.IntegerField()
