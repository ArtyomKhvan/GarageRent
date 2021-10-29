from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Client


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/index.html")


