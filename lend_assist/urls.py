from django.urls import path

from .models import Neighbour
from .views import (
    index,
    NeighbourListView,
    ServiceListView,
    RequestListView,
    NeighbourDetailView,
    ServiceDetailView,
    RequestDetailView,
    NeighbourCreateView,
    ServiceCreateView,
    RequestCreateView,
    NeighbourUpdateView,
    ServiceUpdateView,
    RequestUpdateView,
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
        "users/create/",
        NeighbourCreateView.as_view(),
        name="user-create",
    ),
    path(
        "users/<int:pk>/update/",
        NeighbourUpdateView.as_view(),
        name="user-update",
    ),

    path(
        "services/",
        ServiceListView.as_view(),
        name="service-list",
    ),
    path(
        "services/<int:pk>/",
        ServiceDetailView.as_view(),
        name="service-detail",
    ),
    path(
        "services/create/",
        ServiceCreateView.as_view(),
        name="service-create",
    ),
    path(
        "services/<int:pk>/update/",
        ServiceUpdateView.as_view(),
        name="service-update",
    ),

    path(
        "requests/",
        RequestListView.as_view(),
        name="request-list",
    ),
    path(
        "requests/<int:pk>/",
        RequestDetailView.as_view(),
        name="request-detail",
    ),
    path(
        "requests/create/",
        RequestCreateView.as_view(),
        name="request-create",
    ),
    path(
        "requests/<int:pk>/update/",
        RequestUpdateView.as_view(),
        name="request-update",
    ),
]

app_name = "lend_assist"