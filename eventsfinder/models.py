from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

ATTENDEE_TYPE_CHOICES = (
        ('O', 'Organizer')
        ('A', 'Attendee'),
        ('S', 'Speaker'),
        ('M', 'Mentor'),
    )

class Event(models.Model):
    creators = models.ManyToManyField(User)
    name = models.CharField(_("Event Name"), max_length=50)
    description = models.TextField(_("Event Description"), null=True, blank=True)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    webste = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)

class Attendee(models.Model):
    attendee = models.ForeignKey(User)
    type = models.CharField(max_length=1, choice=ATTENDEE_TYPE_CHOICES, default='A')
    event = models.ForeignKey(Event)

