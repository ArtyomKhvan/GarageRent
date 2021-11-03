from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from webapp.models import Client


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Client
        exclude = ['created_at', 'author']
