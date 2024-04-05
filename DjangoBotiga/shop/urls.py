# En miapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Aquí puedes añadir el nombre 'product_list' si deseas
    path("cat/<int:category_id>/", views.product_category, name='product_category'),
]
