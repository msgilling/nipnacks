from django.db import models

# Create your models here.
class Pot(models.Model):
    name = models.CharField(max_length=100, default=None)
    image = models.CharField(max_length=500, default=None)
    description = models.CharField(max_length=500, default=None)
    small_print = models.CharField(max_length=500, default=None)
    height_cm = models.DecimalField(max_digits=3, decimal_places=1)
    width_cm = models.DecimalField(max_digits=3, decimal_places=1)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name}'

        