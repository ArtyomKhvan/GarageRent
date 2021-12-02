from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    model = models.CharField(max_length=30, null=False, blank=False, verbose_name=_("Model"))
    volume = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False, verbose_name=_("Vol"))
    year = models.DateField(blank=False, null=False)
    fuel = models.CharField(max_length=30, blank=True, null=True, verbose_name=_("Fuel"))
    platform = models.ForeignKey("webapp.Platform", on_delete=models.PROTECT, verbose_name=_("Platform"),
                                 related_name="cars")

    def __str__(self):
        return f"{self.model} - {self.fuel} - {self.platform}"


class Photo(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to="photos", verbose_name=_("Photo"))
    car = models.ForeignKey("webapp.Car", null=False, blank=False, on_delete=models.CASCADE, verbose_name=_("Car"),
                            related_name="photos")

    def __str__(self):
        return f"{self.pk}"


class Platform(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name=_("Model"))
    length = models.PositiveSmallIntegerField(blank=False, null=False, verbose_name=_("LongPla"))
    width = models.PositiveSmallIntegerField(blank=False, null=False, verbose_name=_("WidthPla"))
    height = models.PositiveSmallIntegerField(blank=False, null=False, verbose_name=_("HeightPla"))

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    car = models.ForeignKey("webapp.Car", on_delete=models.CASCADE, verbose_name=_("Model"), related_name="reviews")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("Author"), related_name="reviews")
    text = models.TextField(max_length=500, verbose_name=_("Review"))
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.car} - {self.author}"


class Client(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name=_('Author'), related_name='clients', on_delete=models.PROTECT)
    phone = PhoneNumberField(blank=True, verbose_name=_("Phone"))
    email = models.EmailField(null=True, blank=True, verbose_name=_("Email"))
    message = models.CharField(max_length=3000, null=False, blank=False, verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now=True)
