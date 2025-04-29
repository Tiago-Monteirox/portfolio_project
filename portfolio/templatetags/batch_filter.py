# portfolio/templatetags/batch_filter.py
from django import template

register = template.Library()

@register.filter
def batch(iterable, n=1):
    length = len(iterable)
    for ndx in range(0, length, n):
        yield iterable[ndx:min(ndx + n, length)]