"""Custom filters for minerals application."""

import random
from django import template
from minerals.models import Mineral

register = template.Library() # pylint: disable=C0103

@register.filter('string_only')
def string_only(string):
    '''Removes special characters from name'''
    simple_string = ""
    for i in string:
        if i.isalpha():
            simple_string = "".join([simple_string, i])
    return simple_string

@register.filter('random_mineral')
def random_mineral(filter_param):
    '''Generates random mineral.'''
    minerals = Mineral.objects.all() # pylint: disable=E1101
    random_m = random.choice(minerals)
    return random_m.pk

@register.filter('image_url')
def image_url(mineral):
    '''Generates url path for image based on mineral.'''
    image_filename = mineral.image_filename
    img_pth = f"images/{image_filename}"
    return img_pth

@register.filter('mineral_attr')
def mineral_attr(attribute):
    """Filter for common_attributes function to return attribute."""
    return attribute[0]

@register.filter('mineral_value')
def mineral_value(attribute):
    """Filter for common_attributes function to return value."""
    return attribute[1]
