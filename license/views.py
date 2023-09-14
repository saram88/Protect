from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem

# Create your views here.


@login_required
def licences(request):
    """ A view to return the license page """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in users can do that.')
        return redirect(reverse('home'))

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'license/my_licenses.html'
    context = {
        'orders': orders,
        'from_profile': True
    }

    return render(request, template, context)


@login_required
def licence(request, order_number):
    """ A view to return the license page """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in users can do that.')
        return redirect(reverse('home'))

    order = get_object_or_404(Order, order_number=order_number)

    template = 'license/license.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def validate_license(request):
    """ A view to return the validate page """

    if request.method == 'POST':
        key = request.POST.get('license_key')

        if key:
            order_line = OrderLineItem.objects.filter(license_key=key)

            if order_line.count() > 0:
                template = 'license/validate_license.html'
                context = {
                    'order_line': order_line,
                    'is_checked': True
                }
                messages.success(request, 'This is a valid license')
                return render(request, template, context)

        template = 'license/validate_license.html'
        context = {
            'is_checked': True
        }

        messages.warning(request, 'This is NOT a valid license')
        return render(request, template, context)

    else:
        template = 'license/validate_license.html'
        context = {
            'is_checked': False,
        }

    return render(request, template, context)
