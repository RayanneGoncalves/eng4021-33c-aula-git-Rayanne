from django.db import models

class Dance(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField()
  nome = models.CharField(max_length=100)
  done = models.BooleanField()

class Passos(models.Model):
  title = models.CharField(max_length = 70)
  nome = models.CharField(max_length=30)
  sobrenome = models.CharField(max_length=50)
  data = models.DateField()
  done = models.BooleanField()