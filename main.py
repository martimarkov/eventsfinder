import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'eventsfinder.settings'

# Google App Engine imports.
from google.appengine.ext.webapp import util
from google.appengine.dist import use_library

#os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
#sys.path.append("/home/brox/tmp/mysite")

use_library('django', '1.5')

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch.dispatcher

# Log errors.
#import logging
#def log_exception(*args, **kwds):
#    logging.exception('Exception in request:')
#
#django.dispatch.dispatcher.connect(
#   log_exception, django.core.signals.got_request_exception)

# Unregister the rollback event handler.
django.dispatch.dispatcher.disconnect(
    django.db._rollback_on_exception,
    django.core.signals.got_request_exception)

def main():
  # Create a Django application for WSGI.
  application = django.core.handlers.wsgi.WSGIHandler()

  # Run the WSGI CGI handler with that application.
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()
