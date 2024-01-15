from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from profiles.models import UserProfile


def bag_contents(request):

    bag_items = []
    total = 0.0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item in bag.items():
        if isinstance(item, int):
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
            product = get_object_or_404(Product, pk=item_id)
            for year, units in item['units_by_year'].items():
                y = int(year)
                if product.discount:
                    new_price = float(
                        product.price - (product.price*product.discount/100)
                    )
                    total += (y * units * new_price)
                    product_price = round(new_price, 2)
                else:
                    total += (y * units * float(product.price))
                    product_price = round(product.price, 2)

                product_count += units
                bag_items.append({
                        'item_id': item_id,
                        'units': units,
                        'unit_price': units * y,
                        'product': product,
                        'product_price': product_price,
                        'unit_price_year': round(y * product_price, 2),
                        'years': year,
                    })

    vat = total * float(settings.STANDARD_VAT_PERCENTAGE / 100)
    grand_total = vat + total

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        wishlist = profile.wishlist.all()
    else:
        wishlist = None

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'vat': vat,
        'vat_percentage': settings.STANDARD_VAT_PERCENTAGE,
        'grand_total': grand_total,
        'wishlist': wishlist
    }

    return context
