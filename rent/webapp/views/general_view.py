from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView, ListView

from webapp.models import Client


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/index.html")


class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/about_us.html")


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/contacts.html")


class ClientCreateView(CreateView):
    model = Client
    template_name = 'partial/client_form.html'
    fields = ['name', 'phone', 'email', 'message']

    def get_success_url(self):
        return redirect('webapp:index')
