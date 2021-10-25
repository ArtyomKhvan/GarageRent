from django import forms
from webapp.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Client
