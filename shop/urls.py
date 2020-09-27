from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from shop import urls
app_name = 'shop'

urlpatterns = [

    path('',views.shop,name='shop'),
    path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:pk>',views.remove_from_cart,name='remove_from_cart'),
    path('cart/',views.cart,name = 'cart'),
    path('order/',views.order,name = 'order'),
    path('quotation/',views.quotation,name = 'quotation')


]
