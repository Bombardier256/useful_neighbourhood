from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from useful_neighbourhood import settings


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


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
        unique_together = ("description", "name",)
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lend_assist:service-detail", kwargs={"pk": self.pk})


class Neighbour(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=13) # len == 9
    service = models.ManyToManyField(
        Service,
        related_name="neighbours",
        blank=True
    )

    class Meta:
        ordering = ["-username"]

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("lend_assist:user-detail", kwargs={"pk": self.pk})


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

    def get_absolute_url(self):
        return reverse("lend_assist:request-detail", kwargs={"pk": self.pk})
