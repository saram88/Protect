from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

import json

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a units of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    units = int(request.POST.get('units'))
    year = int(request.POST.get('years'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})
        
    if item_id in list(bag.keys()):
        cart = json.loads(bag[item_id])

        if 'year' in cart.keys():
            cart["year"][0] += year
            cart["unit"][0] += units
            bag[item_id] = json.dumps(cart, default=set_default)
            messages.success(request, f'1. Updated {units} {product.name} with {year} to {cart["unit"][0]} units')
        else:
            #cart["year"][0] = year
            #cart["unit"][0] = units
            bag[item_id] = json.dumps({'year': {year}, 'unit': {units} }, default=set_default)
            messages.success(request, f'2. Added {units} {product.name} for {year} year(s) to your bag')
    else:
        bag[item_id] = json.dumps({'year': {year}, 'unit': {units} }, default=set_default)
        messages.success(request, f'3. Added {units} {product.name} for {year} year(s) to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the units of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    units = int(request.POST.get('units'))
    year = int(request.POST.get('years'))

    bag = request.session.get('bag', {})

    cart = json.loads(bag[item_id])

    if units > 0:
        cart["year"][0] = year
        cart["unit"][0] = units
        bag[item_id] = json.dumps(cart, default=set_default)
        messages.success(request, f'6. Updated {units} {product.name} with {year} to {cart["unit"][0]} units')
    else:
        bag.pop(item_id)
        messages.success(request, f'7. Removed {product.name} from your bag')
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError