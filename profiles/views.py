from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, UserWishlist
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = profile.wishlist.all()

    template = 'profiles/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)

@login_required
def add_to_wishlist(request, product_id):

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you have to log in to add a to wishlist.')
        return redirect(reverse('products'))
    
    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    
    wished_product,created = UserWishlist.objects.get_or_create(
        wished_product=product,
        user_profile = profile,
    )
    messages.success(request,'The product was added to your wishlist')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def remove_from_wishlist(request, wishlist_id):
    """ Delete a wishlist """

    wishlist = get_object_or_404(UserWishlist, pk=wishlist_id)
    wishlist.delete()
    messages.success(request, 'Product removed from wishlist!')
    return redirect(reverse('wishlist'))
