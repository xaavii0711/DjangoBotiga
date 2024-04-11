# En miapp/urls.py
from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Aquí puedes añadir el nombre 'product_list' si deseas
    path("cat/<int:category_id>/", views.product_category, name='product_category'),
    path('api/prods', api.getProducts),
    path('api/prods/<int:category_id>', api.getProductsByCategory),
    path('carrito/', views.carrito, name='carrito'),  # Vista del carrito de compras
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), 
]
