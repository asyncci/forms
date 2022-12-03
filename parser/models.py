from django.db import models

# Create your models here.

class Car(models.Model):
    year = models.CharField(max_length=10)
    image = models.ImageField(upload_to="parser/images/")
    price = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)

    def __str__(self):
        return self.car_model
    