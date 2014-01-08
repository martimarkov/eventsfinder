from django.core.mail import EmailMultiAlternatives, send_mail
from google.appengine.api import mail
import threading

# Send emails asynchronously
class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
        msg.send(self.fail_silently)

def send_async_mail(subject, body, from_email, recipient_list, fail_silently=False, html=None, *args, **kwargs):
#    EmailThread(subject, body, from_email, recipient_list, fail_silently, html).start()
#    send_mail(subject, body, from_email, recipient_list)
    send_mail("hello", "world", "hackasoton@gmail.com", ["axsauze@gmail.com"])

