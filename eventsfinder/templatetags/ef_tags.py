from django import template
from eventsfinder.models import Event, Attendee

register = template.Library()

@register.assignment_tag(takes_context=True)
def is_attending(context, event):
    user = context['request'].user

    attending = False
    try:
        attendee = Attendee.objects.get(attendee=user, event=event)
        attending = attendee.type == 'A'

    except Exception:
        pass

    return 1 if attending else 0

@register.assignment_tag(takes_context=True)
def is_tracking(context, event):
    user = context['request'].user

    tracking = False
    try:
        attendee = Attendee.objects.get(attendee=user, event=event)
        tracking = attendee.type == 'T'

    except Exception:
        pass

    return 1 if tracking else 0
