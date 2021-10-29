from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView, ListView
from webapp.models import Car


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/index.html")


class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/about_us.html")


class CarListView(ListView):
    model = Car
    template_name = "cars/list.html"
    ordering = ["year"]
    context_object_name = "cars"

