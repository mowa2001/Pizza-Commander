from django.urls import path
from . import views

#app_name = 'food'

urlpatterns = [
   path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('add_to_cart/<int:pizza_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
