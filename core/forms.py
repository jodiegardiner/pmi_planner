from django import forms
import datetime
from django.core.exceptions import ValidationError


class ClientCreationForm(forms.Form):

    PACKAGE_CHOICES = [(i, i,) for i in xrange(4, 37, 2)]

    client_name = forms.CharField(label="Client name", initial='enter a name')
    notes = forms.CharField(widget=forms.Textarea, initial="notes")
    purchased_plan = forms.ChoiceField(label="Plan", choices=PACKAGE_CHOICES)
    due_date = forms.DateField(initial=(datetime.date.today() + datetime.timedelta(days=240)))