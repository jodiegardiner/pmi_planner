from django import forms
import datetime
from django.core.exceptions import ValidationError
from .models import Client


class ClientCreationForm(forms.Form):

    PACKAGE_CHOICES = [(i, i,) for i in xrange(4, 37, 2)]

    client_name = forms.CharField(label="Client name", required=True)
    client_address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    client_email = forms.EmailField(label="Client email", required=False)
    client_phone = forms.CharField(label="Phone", max_length=15, required=False)
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)
    purchased_plan = forms.ChoiceField(label="Care commences in week:", choices=PACKAGE_CHOICES)
    # due_date = forms.DateField(initial=(datetime.date.today() + datetime.timedelta(days=240)))


    class Meta:
        model = Client
        fields = ['name', 'address', 'email', 'phone', 'notes']

    def save(self, commit=True):
        instance = super(ClientCreationForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance
