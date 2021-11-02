from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView, ListView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/index.html")


class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/about_us.html")


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/contacts.html")

