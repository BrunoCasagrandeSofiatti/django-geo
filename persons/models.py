from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
