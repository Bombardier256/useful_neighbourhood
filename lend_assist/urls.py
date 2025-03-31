from django.urls import path

from .views import (
    index,
    ServiceListView,
    RequestListView,
    NeighbourDetailView,
    ServiceDetailView,
    RequestDetailView,
    NeighbourCreateView,
    NeighbourUpdateView,
    ServiceUpdateView,
    RequestUpdateView,
    NeighbourDeleteView,
    ServiceDeleteView,
    RequestDeleteView,
    create_service,
    create_request,
    RentalListView,
    ServiceAddNeighbourView,
    ServiceRemoveNeighbourView,
    RequestAddNeighbourView,
    RequestRemoveNeighbourView,
)


urlpatterns = [
    path("", index, name="index"),
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
        "rentals/",
        RentalListView.as_view(),
        name="rental-list",
    ),
    path(
        "services/<int:pk>/",
        ServiceDetailView.as_view(),
        name="service-detail",
    ),
    path(
        "services/create/",
        create_service,
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
        "services/<int:serv_pk>/neighobour_add/",
        ServiceAddNeighbourView.as_view(),
        name="service-neighbour-add"
    ),
    path(
        "services/<int:serv_pk>/neighobour_remove/",
        ServiceRemoveNeighbourView.as_view(),
        name="service-neighbour-remove"
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
        create_request,
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
    path(
        "requests/<int:req_pk>/neighobour_add/",
        RequestAddNeighbourView.as_view(),
        name="request-neighbour-add"
    ),
    path(
        "requests/<int:req_pk>/neighobour_remove/",
        RequestRemoveNeighbourView.as_view(),
        name="request-neighbour-remove"
    ),
]

app_name = "lend_assist"
