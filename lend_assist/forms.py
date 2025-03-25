from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from lend_assist.models import (
    Neighbour,
    Service,
    Request,
)

from django.core.validators import RegexValidator
from django.db import models


validate_phone = RegexValidator(
    regex=r'^\+?1?\d{12,12}$',
    message="Phone number must be entered in the format: '+380501234567'. Only 12 digits are allowed."
)

def validate_capitalize(word: str) -> None:
    if not word[0].isupper():
        raise ValidationError("Name must start with a capital letter.")

class NeighbourCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField(validators=[validate_phone])
    email = forms.EmailField()

    class Meta:
        model = Neighbour
        fields = ("username", "password", "first_name", "last_name", "phone", "address", "email",)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class NeighbourUpdateForm(forms.ModelForm):
    class Meta:
        model = Neighbour
        fields = ("username", "first_name", "last_name", "phone", "address", "email")


class ServiceCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, validators=[validate_capitalize])
    class Meta:
        model = Service
        exclude = ("neighbours", "author_username")


class ServiceUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, validators=[validate_capitalize])
    class Meta:
        model = Service
        exclude = ("neighbours", "author_username")


class RequestCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, validators=[validate_capitalize])
    class Meta:
        model = Request
        exclude = ("neighbours", "author_username")


class RequestUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, validators=[validate_capitalize])
    class Meta:
        model = Request
        exclude = ("neighbours", "author_username")


class SearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )
