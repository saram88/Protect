from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a units of the specified product to the shopping bag """

    units = int(request.POST.get('units'))
    redirect_url = request.POST.get('redirect_url')
    year = int(request.POST.get('years'))
#    if 'years' in request.POST:
#        year = int(request.POST['product_year'])
    bag = request.session.get('bag', {})

    if year:
        if item_id in list(bag.keys()):
            if year in bag[item_id]['years'].keys():
                bag[item_id]['years'][year] += units
            else:
                bag[item_id]['years'][year] = units
        else:
            bag[item_id] = {'years': {year: units}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += (units * year)
        else:
            bag[item_id] = (units * year)

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the units of the specified product to the specified amount"""

    units = int(request.POST.get('units'))
    year = int(request.POST.get('years'))
#    if 'product_year' in request.POST:
#        year = int(request.POST['product_year'])
    bag = request.session.get('bag', {})

#    if year:
#        if units > 0:
#            bag[item_id]['years'][year] = units
#        else:
#            del bag[item_id]['years'][year]
#            if not bag[item_id]['years']:
#                bag.pop(item_id)
#    else:
    if units > 0:
        bag[item_id] = (units * year)
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)