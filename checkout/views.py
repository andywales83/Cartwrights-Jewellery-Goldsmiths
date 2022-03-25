"""
Checkout, Checkout Success and Cache Checkout Data views
"""
from django.shortcuts import render, redirect, reverse

from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    A view to show checkout data
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket yet.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
    }

    return render(request, template, context)
