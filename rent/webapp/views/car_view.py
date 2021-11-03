from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, ListView

from webapp.forms import CarForm, PhotoForm
from webapp.models import Car, Review, Photo


class CarListView(ListView):
    model = Car
    template_name = "cars/list.html"
    ordering = ["year"]
    context_object_name = "cars"


class CarDetailView(DetailView):
    model = Car
    template_name = "cars/detail.html"
    context_object_name = "car"
    pk_url_kwarg = "pk"


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'partial/review_form.html'
    fields = ['text']

    def form_valid(self, form):
        form.instance.car = self.get_object()
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Car, pk=pk)

    def get_success_url(self):
        return reverse('webapp:car_detail', kwargs={"pk": self.object.car.pk})


class CarCreateView(PermissionRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = "cars/create.html"
    permission_required = "webapp.add_car"

    def get_form(self, form_class=None):
        form = super().get_form()
        form.helper.form_action = 'webapp:car_create'
        return form

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Car, pk=pk)

    def get_success_url(self):
        return reverse('webapp:car_detail', kwargs={"pk": self.object.pk})


class CarDeleteView(PermissionRequiredMixin, DeleteView):
    model = Car
    template_name = "cars/delete.html"
    success_url = reverse_lazy("webapp:index")
    permission_required = "webapp.delete_car"


class PhotoCreateView(PermissionRequiredMixin, CreateView):
    model = Photo
    template_name = "cars/photo_form.html"
    form_class = PhotoForm
    permission_required = "webapp.add_photo"

    def form_valid(self, form):
        form.instance.car = self.get_object()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["pk"] = self.kwargs.get("pk")
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Car, pk=pk)

    def get_success_url(self):
        return reverse('webapp:car_detail', kwargs={"pk": self.object.car.pk})
