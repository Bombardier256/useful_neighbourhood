from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from lend_assist.forms import (
    NeighbourCreateForm,
    ServiceCreateForm,
    RequestCreateForm,
    NeighbourUpdateForm,
)
from lend_assist.models import Service, Neighbour, Request


def index(request):
    """View function for the home page of the site."""

    num_users = Neighbour.objects.count()
    num_services = Service.objects.count()
    num_requests = Request.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_users": num_users,
        "num_services": num_services,
        "num_requests": num_requests,
        "num_visits": num_visits + 1,
    }

    return render(request, "lend_assist/index.html", context=context)


class NeighbourListView(generic.ListView):
    model = Neighbour
    context_object_name = "user_list"
    template_name = "lend_assist/user_list.html"
    paginate_by = 10


class NeighbourDetailView(generic.DetailView):
    model = Neighbour
    success_url = reverse_lazy("lend_assist:user_list")
    template_name = "lend_assist/user_detail.html"
    context_object_name = "user"


class NeighbourCreateView(generic.CreateView):
    model = Neighbour
    form_class = NeighbourCreateForm
    success_url = reverse_lazy("lend_assist:service-list")
    template_name = "lend_assist/user_form.html"


class NeighbourUpdateView(generic.UpdateView):
    model = Neighbour
    form_class = NeighbourUpdateForm
    success_url = reverse_lazy("lend_assist:service-list")
    template_name = "lend_assist/user_form.html"


class ServiceListView(generic.ListView):
    model = Service
    template_name = "lend_assist/service_list.html"
    paginate_by = 10

class ServiceDetailView(generic.DetailView):
    model = Service


class ServiceCreateView(generic.CreateView):
    model = Service
    form_class = ServiceCreateForm
    success_url = reverse_lazy("lend_assist:service-list")


class RequestListView(generic.ListView):
    model = Request
    template_name = "lend_assist/request_list.html"
    paginate_by = 10


class RequestDetailView(generic.DetailView):
    model = Request


class RequestCreateView(generic.CreateView):
    model = Request
    form_class = RequestCreateForm
    success_url = reverse_lazy("lend_assist:request-list")
