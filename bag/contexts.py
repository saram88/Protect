from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, units in bag.items():
        if isinstance(units, int):
            product = get_object_or_404(Product, pk=item_id)
            total += units * product.price
            product_count += units
            bag_items.append({
                'item_id': item_id,
                'units': units,
                'product': product,
                'years': 1,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for year, units in units['years'].items():
                total += units * product.price
                product_count += units
                bag_items.append({
                    'item_id': item_id,
                    'units': units,
                    'product': product,
                    'year': year,
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