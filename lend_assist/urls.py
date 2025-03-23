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
    NeighbourDeleteView,
    ServiceDeleteView,
    RequestDeleteView,
    service_neighbour_add,
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
        "users/<int:pk>/delete/",
        NeighbourDeleteView.as_view(),
        name="user-delete",
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
        "services/<int:pk>/delete/",
        ServiceDeleteView.as_view(),
        name="service-delete",
    ),
    path(
        "services/<int:serv_pk>/neighobour_add/<int:user_pk>",
        service_neighbour_add, name="service-neighbour-add"
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
    path(
        "requests/<int:pk>/delete/",
        RequestDeleteView.as_view(),
        name="request-delete",
    ),
]

app_name = "lend_assist"