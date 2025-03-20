from django.urls import path

from .models import Neighbour
from .views import (
    index,
    NeighbourListView,
    ServiceListView,
    RequestListView,
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "users/",
        NeighbourListView.as_view(),
        name="user-list",
    ),

    path(
        "services/",
        ServiceListView.as_view(),
        name="service-list",
    ),
    path(
        "requests/",
        RequestListView.as_view(),
        name="request-list",
    ),
]

app_name = "lend_assist"