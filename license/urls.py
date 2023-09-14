from django.urls import path
from . import views

urlpatterns = [
    path('', views.licences, name='licenses'),
    path('<order_number>', views.licence, name='order_license'),
    path('validate/', views.validate_license, name='validate'),
]
