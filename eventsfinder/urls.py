from django.conf.urls.defaults import *
from eventsfinder import views, ajax
from django.contrib import admin
import dbindexer
from django.conf.urls import patterns

handler500 = 'djangotoolbox.errorviews.server_error'

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'eventsfinder.views.handler404'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),

    url(r'^$', views.home, name='home'),
    url(r'^find/$', views.find_events, name='find_events'),
    url(r'^create/$', views.add_event, name='add_event'),
    url(r'^manage/$', views.manage_events, name='manage_events'),
    url(r'^manage/(?P<event_id>.+)/$', views.view_event, name='manage_events'),

    # Handling all AJAX calls
    url(r'^attend_event/$', ajax.attend_event, name='attend_event'),

    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}),
    (r'^signup/$', views.signup),


    ('^admin/', include(admin.site.urls)),
)
