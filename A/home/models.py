from django.db import models

class Tire(models.Model) :
    tire_name = models.CharField(max_length = 10)
    tire_description = models.CharField(max_length = 100)
    tire_price = models.IntegerField()

    def __str__(self):
        return self.tire_name

class ContactForm(models.Model):
    contact_name = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=15)
    contact_body = models.CharField(max_length=500)
    contact_email = models.EmailField() 

    def __str__(self):
        return self.contact_name