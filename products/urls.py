from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path(
        '<int:product_id>',
        views.product_detail,
        name='product_detail'
    ),
    path(
        'add/',
        views.add_product,
        name='add_product'
    ),
    path(
        'edit/<int:product_id>/',
        views.edit_product,
        name='edit_product'
    ),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    ),
    path(
        'review/<int:product_id>/',
        views.add_review,
        name='add_review'
    ),
    path(
        'review/delete/<int:review_id>/',
        views.delete_review,
        name='delete_review'
    ),
    path(
        'download/<path>/',
        views.download_file,
        name='download_file'
    ),
]
