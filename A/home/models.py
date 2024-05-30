from django.db import models

class Tire(models.Model) :
    tire_name = models.CharField(max_length = 10)
    tire_description = models.CharField(max_length = 100)
    tire_price = models.IntegerField()

    def __str__(self):
        return self.tire_name
