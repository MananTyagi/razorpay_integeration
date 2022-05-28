from django.urls import path, include
from .views import *


urlpatterns=[
    path('', coffee_payment, name="coffee_payment"),
    path('payment_status/',payment_status, name="payment_status"),
]