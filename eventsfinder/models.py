from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django import forms

from djangotoolbox.fields import ListField


ATTENDEE_TYPE_CHOICES = (
        ('A', 'Attendee'),
        ('T', 'Tracker'),
    )

STAFF_TYPE_CHOICES = (
        ('O', 'Organizer'),
        ('S', 'Speaker'),
        ('M', 'Mentor'),
    )

class StringListField(forms.CharField):

    def prepare_value(self, value):
        return ', '.join(value)

    def to_python(self, value):
        if not value:
            return []
        return [item.strip() for item in value.split(',')]

class Tag(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)


# TODO add sponsors!!
class Event(models.Model):
    creator = models.OneToOneField(User)
    name = models.CharField(_("Event Name"), max_length=50)
    description = models.TextField(_("Event Description"), null=True, blank=True)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    website = models.CharField(max_length=100, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    tags = Tag()

    def get_address_array(self):
        return [ self.address, self.country, self.city, self.zip ]

    def get_short_address(self):
        return self.zip + " " + self.city + ", " + self.country

class Attendee(models.Model):
    attendee = models.ForeignKey(User)
    type = models.CharField(max_length=1, choices=ATTENDEE_TYPE_CHOICES, default='A')
    event = models.ForeignKey(Event)

class Staff(models.Model):
    staff = models.ForeignKey(User, null=True, blank=True)

    name = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=120)

    type = models.CharField(max_length=1, choices=STAFF_TYPE_CHOICES, default='M')
    event = models.ForeignKey(Event)