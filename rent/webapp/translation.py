from modeltranslation.translator import translator, TranslationOptions
from .models import Car


class CarTranslationOptions(TranslationOptions):
    fields = ("model", "fuel")


translator.register(Car, CarTranslationOptions)
