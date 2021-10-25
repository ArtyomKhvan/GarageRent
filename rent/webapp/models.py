from django.db import models
from django.contrib.auth import get_user_model


class Car(models.Model):
    model = models.CharField(max_length=30, null=False, blank=False, verbose_name="Модель")
    volume = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False, verbose_name="объём")
    year = models.DateField(blank=False, null=False)
    fuel = models.CharField(max_length=30, blank=True, null=True, verbose_name="Топливо")
    platform = models.ForeignKey("webapp.Platform", on_delete=models.PROTECT, verbose_name="Платформа",
                                 related_name="cars")


class Photo(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to="photos", verbose_name="Фотография")


class Platform(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name="Модель")
    length = models.PositiveSmallIntegerField(blank=False, null=False, verbose_name="Длинна в см")
    width = models.PositiveSmallIntegerField(blank=False, null=False, verbose_name="Ширина в см")
    height = models.PositiveSmallIntegerField(blank=False, null=False, verbose_name="Высота в см")


class Review(models.Model):
    car = models.ForeignKey("webapp.Car", on_delete=models.CASCADE, verbose_name="Отзыв", related_name="reviews")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Автор", related_name="reviews")
    text = models.TextField(max_length=500, verbose_name="Отзыв")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
