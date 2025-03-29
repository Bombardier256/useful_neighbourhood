from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from useful_neighbourhood import settings


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Neighbour(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=13) # len == 9

    class Meta:
        ordering = ["-username"]

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse(
            "lend_assist:user-detail",
            kwargs={"pk": self.pk}
        )


class Service(models.Model):
    name = models.CharField(max_length=255)
    author_username = models.CharField(max_length=50)
    description = models.TextField()
    free_of_charge = models.BooleanField(default=True)
    is_lending = models.BooleanField(default=False)
    neighbours = models.ManyToManyField(
        Neighbour,
        related_name="services"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="services"
    )


    class Meta:
        unique_together = ("description", "name",)
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "lend_assist:service-detail",
            kwargs={"pk": self.pk}
        )


class Request(models.Model):
    name = models.CharField(max_length=255)
    author_username = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    complete = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="requests"
    )
    neighbours = models.ManyToManyField(
        Neighbour,
        related_name="requests"
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "lend_assist:request-detail",
            kwargs={"pk": self.pk}
        )
