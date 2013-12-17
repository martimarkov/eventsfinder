from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from eventsfinder.models import Event


class EventCreationForm(forms.ModelForm):
    error_messages = {
        'invalid_address': _("Please provide a valid address.")
        }

    class Meta:
        model = Event
        exclude = ['creator']

    def save(self, commit=True):
        event = super(EventCreationForm, self).save(commit=False)
        if commit:
            event.save()
        return event
