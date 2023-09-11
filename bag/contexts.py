from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

import json


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item in bag.items():
        if isinstance(item, int):
            print('isinstance(units, int):')

            product = get_object_or_404(Product, pk=item_id)
            total += item * product.price
            product_count += item
            bag_items.append({
                'item_id': item_id,
                'units': item,
                'product': product,
                'years': 1,
            })
        else:
            cart = json.loads(bag[item_id])
            product = get_object_or_404(Product, pk=item_id)
            total = total + cart["year"][0] * cart["unit"][0] * product.price
            product_count = cart["unit"][0] * cart["year"][0]
            bag_items.append({
                    'item_id': item_id,
                    'units': cart["unit"][0],
                    'unit_price': cart["unit"][0] * cart["year"][0],
                    'product': product,
                    'years': cart["year"][0],
                })

    vat = total * Decimal(settings.STANDARD_VAT_PERCENTAGE / 100)
    grand_total = vat + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'vat': vat,
        'vat_percentage': settings.STANDARD_VAT_PERCENTAGE,
        'grand_total': grand_total,
    }

    return context