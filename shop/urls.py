from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('contact/', views.contact_view, name='contact'),
    path('moreproducts/', views.more_products_view, name='moreproducts'),
    path('shop/', views.shop_view, name='shop'),
    path('search/', views.search_view, name='search_results'),
    path('shop/category/<str:category_name>/', views.products_by_category, name='products_by_category'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
