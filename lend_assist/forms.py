from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from lend_assist.models import (
    Neighbour,
    Service,
    Request,
)


class NeighbourCreateForm(forms.ModelForm):
    class Meta:
        model = Neighbour
        fields = ("username", "first_name", "last_name", "phone", "address", "email")