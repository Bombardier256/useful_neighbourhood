from django.urls import path

from .models import Neighbour
from .views import (
    index,
    NeighbourListView,
    ServiceListView,
    RequestListView,
    NeighbourDetailView,
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "users/",
        NeighbourListView.as_view(),
        name="user-list",
    ),
    path(
        "users/<int:pk>/",
        NeighbourDetailView.as_view(),
        name="user-detail",
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