from django.contrib.auth.models import AbstractUser
from django.db import models

from useful_neighbourhood import settings


class Section(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Service(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="services"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    free_of_charge = models.BooleanField(default=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ("section", "name",)
        ordering = ["name"]

    def __str__(self):
        return self.name


class Lending(Service):
    deposit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )


class Neighbour(AbstractUser):
    service = models.ManyToManyField(Service, related_name="n-service", blank=True)
    lending = models.ManyToManyField(Lending, related_name="n-lending", blank=True)
    apartment = models.IntegerField() # 1 - 1000
    #phone = models.IntegerField() # len == 9

    class Meta:
        ordering = ["apartment"]

    def __str__(self):
        return f"({self.first_name} app. {self.apartment})"


class Request(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="requests"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
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
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name
