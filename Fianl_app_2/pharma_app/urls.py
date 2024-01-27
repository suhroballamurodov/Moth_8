from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('cart', cart, name='cart'),
    path('thankyou', thankyou, name='thankyou'),
    path('shop', shop, name='shop'),
    path('shop-single', shop_single, name='shop-single'),
    path('checkout', checkout, name='checkout'),
]