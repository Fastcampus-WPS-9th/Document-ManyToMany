from django.db import models

__all__ = (
    'Topping',
    'Pizza',
)


class Topping(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=10)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name
