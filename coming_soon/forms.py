from django import forms

from coming_soon.models import Clients


class ClientForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = ['email_address']

