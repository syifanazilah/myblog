from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def strip_tags_filter(value):
    return strip_tags(value)
