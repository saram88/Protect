from django.contrib import admin
from .models import Product, Category

# register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'catagory',
        'price',
        'discount',
        'rating',
        'image'
    )

    ordering = ('sku',)


class CatagoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CatagoryAdmin)