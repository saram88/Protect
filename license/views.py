from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order, OrderLineItem

# Create your views here.


@login_required
def licences(request):
    """ A view to return the license page """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in users can do that.')
        return redirect(reverse('home'))

    template = 'license/my_licenses.html'
    context = {
    }

    return render(request, template, context)

@login_required
def licence(request, order_number):
    """ A view to return the license page """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in users can do that.')
        return redirect(reverse('home'))

    order = get_object_or_404(Order, order_number=order_number)
    order_line = get_object_or_404(OrderLineItem, order=order.id)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'license/license.html'
    context = {
        'order': order,
        'order_line': order_line,
        'from_profile': True,
    }

    return render(request, template, context)

def validate_license(request):
    """ A view to return the validate page """

    template = 'license/validate_license.html'
    context = {
    }

    return render(request, template, context)