from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from lend_assist.forms import (
    NeighbourCreateForm,
    ServiceCreateForm,
    RequestCreateForm,
    SearchForm,
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


class NeighbourDetailView(LoginRequiredMixin, generic.DetailView):
    model = Neighbour
    success_url = reverse_lazy("lend_assist:user_list")
    template_name = "lend_assist/user_detail.html"


class NeighbourCreateView(generic.CreateView):
    model = Neighbour
    form_class = NeighbourCreateForm
    success_url = reverse_lazy("lend_assist:service-list")
    template_name = "lend_assist/user_form.html"


class NeighbourUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Neighbour
    form_class = NeighbourCreateForm
    success_url = reverse_lazy("lend_assist:service-list")
    template_name = "lend_assist/user_form.html"


class NeighbourDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Neighbour
    success_url = reverse_lazy("lend_assist:index")
    template_name = "lend_assist/user_confirm_delete.html"


class ServiceListView(LoginRequiredMixin, generic.ListView):
    model = Service
    template_name = "lend_assist/service_list.html"
    paginate_by = 5
    queryset = Service.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = SearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        title = self.request.GET.get("title")
        if title:
            return self.queryset.filter(name__contains=title)

        return self.queryset



class ServiceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Service


def create_service(request):
    neighbour = Neighbour.objects.get(pk=request.user.pk)

    if not neighbour:
        return redirect("lend_assist:user-create")

    if request.method == "POST":
        form = ServiceCreateForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            service.neighbours.add(neighbour)
            service.author_username = neighbour.username
            service.save()

            return redirect("lend_assist:service-list")

    else:
        form = ServiceCreateForm()

    return render(request, "lend_assist/service_form.html", {"form": form})


class ServiceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Service
    form_class = ServiceCreateForm
    success_url = reverse_lazy("lend_assist:service-list")


class ServiceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Service
    success_url = reverse_lazy("lend_assist:service-list")


class RequestListView(LoginRequiredMixin, generic.ListView):
    model = Request
    template_name = "lend_assist/request_list.html"
    paginate_by = 5
    queryset = Request.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RequestListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = SearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        title = self.request.GET.get("title")
        if title:
            return self.queryset.filter(name__contains=title)

        return self.queryset

class RequestDetailView(LoginRequiredMixin, generic.DetailView):
    model = Request


def create_request(request_data):
    neighbour = Neighbour.objects.get(pk=request_data.user.pk)

    if not neighbour:
        return redirect("lend_assist:user-create")

    if request_data.method == "POST":
        form = RequestCreateForm(request_data.POST)
        if form.is_valid():
            request = form.save(commit=False)
            request.save()
            request.neighbours.add(neighbour)
            request.author_username = neighbour.username
            request.save()

            return redirect("lend_assist:request-list")

    else:
        form = ServiceCreateForm()

    return render(request_data, "lend_assist/request_form.html", {"form": form})


class RequestUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Request
    form_class = RequestCreateForm
    success_url = reverse_lazy("lend_assist:request-list")


class RequestDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Request
    success_url = reverse_lazy("lend_assist:request-list")


def service_neighbour_add(request, serv_pk: int):
    service = Service.objects.get(pk=serv_pk)
    neighbour = Neighbour.objects.get(pk=request.user.pk)
    service.neighbours.add(neighbour)
    return redirect("lend_assist:service-list")


def service_neighbour_remove(request, serv_pk: int):
    service = Service.objects.get(pk=serv_pk)
    neighbour = Neighbour.objects.get(pk=request.user.pk)
    service.neighbours.remove(neighbour)
    return redirect("lend_assist:service-list")


def request_neighbour_add(request_data, req_pk: int):
    request = Request.objects.get(pk=req_pk)
    neighbour = Neighbour.objects.get(pk=request_data.user.pk)
    request.neighbours.add(neighbour)
    return redirect("lend_assist:request-list")

def request_neighbour_remove(request_data, req_pk: int):
    request = Request.objects.get(pk=req_pk)
    neighbour = Neighbour.objects.get(pk=request_data.user.pk)
    request.neighbours.remove(neighbour)
    return redirect("lend_assist:request-list")