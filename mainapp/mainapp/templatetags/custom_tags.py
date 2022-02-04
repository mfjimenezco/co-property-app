"""Custom template tags."""

# Django
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_setting(name):
    """Get setting variable template tag.
    """
    if name.startswith('APP_'):
        return getattr(settings, name, "")
    else:
        return "It is not possible to display this value"
