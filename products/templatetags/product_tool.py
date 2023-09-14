from django import template

register = template.Library()


@register.filter(name='calc_productprice')
def calc_productprice(price, discount):
    return price - round(price * discount / 100, 2)
