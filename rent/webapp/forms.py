from phonenumber_field.formfields import PhoneNumberField
from django import forms


class ClientForm(forms.ModelForm):
    class Meta:
        exclude = []
        phone = PhoneNumberField()
