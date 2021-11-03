from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from webapp.forms import ClientForm
from webapp.models import Client


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/index.html")


class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "general/about_us.html")


class ContactView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'general/contacts.html'
    form_class = ClientForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form()
        form.helper.form_action = 'webapp:contacts'
        return form

    def get_success_url(self):
        return reverse('webapp:index')


