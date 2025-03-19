from django.contrib.auth.models import AbstractUser
from django.db import models

from useful_neighbourhood import settings


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    free_of_charge = models.BooleanField(default=True)
    is_lending = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="services"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ("category", "name",)
        ordering = ["name"]

    def __str__(self):
        return self.name


class Neighbour(AbstractUser):
    service = models.ManyToManyField(Service, related_name="neighbours", blank=True)
    apartment = models.IntegerField() # 1 - 1000
    phone = models.CharField(max_length=13) # len == 9

    class Meta:
        ordering = ["apartment"]

    def __str__(self):
        return f"({self.first_name} app. {self.apartment})"


class Request(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    complete = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="requests"
    )
    neighbour = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="requests"
    )
    reward = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name
