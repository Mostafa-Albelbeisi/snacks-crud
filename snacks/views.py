from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from .models import Snack
from django.urls import reverse_lazy


# Create your views here.


# class HomePage(TemplateView):
#     template_name = "home.html"


class SnackList(ListView):
    template_name = "SnackListView.html"
    model = Snack
    context_object_name = "allSnacks"


class SnackDetail(DetailView):
    template_name = "SnackDetailView.html"
    model = Snack


class SnackCreate(CreateView):
    template_name = "SnackCreateView.html"
    model = Snack
    fields = ["title", "description", "purchaser"]


class SnackUpdate(UpdateView):
    template_name = "SnackUpdateView.html"
    model = Snack
    fields = ["title", "description", "purchaser"]


class SnackDelete(DeleteView):
    template_name = "SnackDeleteView.html"
    model = Snack
    success_url = reverse_lazy("SnackListView")
