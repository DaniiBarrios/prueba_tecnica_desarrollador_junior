from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    cholesterol = models.FloatField()
    heart_rate = models.FloatField()

    def __str__(self):
        return self.name
