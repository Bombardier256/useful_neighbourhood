from django.urls import path

from .models import Neighbour
from .views import (
    index,
    NeighbourListView,
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "users/",
        NeighbourListView.as_view(),
        name="user-list",
    )

]

app_name = "lend_assist"