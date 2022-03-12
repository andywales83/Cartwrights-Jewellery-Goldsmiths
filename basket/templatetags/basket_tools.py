"""
Template tags for basket
"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Template tags for basket to calculate subtotal
    """
    return price * quantity
