from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NNK6eLmy745vH0NxAZi6JgiPA37rt1bSSy4LckYoutbX18uGmxfNs9a6mkd4hY3ma1oR7Bsx4w1Wv8QsunZxV1H00teusjiQf',  # NOQA
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
