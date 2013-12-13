from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'eventsfinder.views.home', name='home'),
    url(r'^add$', 'eventsfinder.views.add_event', name='add_event'),
)
