from django.conf.urls.defaults import *
from django.contrib import admin
import dbindexer
from django.conf.urls import patterns

handler500 = 'djangotoolbox.errorviews.server_error'

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),

    url(r'^/$', 'eventsfinder.views.home', name='home'),
    url(r'^find/$', 'eventsfinder.views.find_events', name='find_events'),
    url(r'^create/$', 'eventsfinder.views.add_event', name='add_event'),
    url(r'^manage/$', 'eventsfinder.views.manage_events', name='manage_events'),

    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}),
    (r'^signup/$', 'eventsfinder.views.signup'),


    ('^admin/', include(admin.site.urls)),
)
