from django.contrib import admin
from .models import Product, Category

# register your models here.
admin.site.register(Product)
admin.site.register(Category)