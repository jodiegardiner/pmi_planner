from django import forms
import datetime
from django.core.exceptions import ValidationError


class ClientCreationForm(forms.Form):

    PACKAGE_CHOICES = [(i, i,) for i in xrange(4, 37, 2)]

    client_name = forms.CharField(label="Client name", required=True)
    client_address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    client_email = forms.EmailField(label="Client email")
    client_phone = forms.CharField(label="Phone", max_length=15)
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    purchased_plan = forms.ChoiceField(label="Care commences in week:", choices=PACKAGE_CHOICES)
    # due_date = forms.DateField(initial=(datetime.date.today() + datetime.timedelta(days=240)))