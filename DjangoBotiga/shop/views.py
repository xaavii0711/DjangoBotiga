from django.shortcuts import render, HttpResponse
from .models import *

def product_list(request):
    categorias = Categoria.objects.all()
    productos = Producte.objects.all()
    return render(request, 'product_list.html', {'categorias': categorias, 'productos': productos})

def product_category(request, category_id):
    # Obtener la categoría específica por su ID
    if category_id:
        categoria = Categoria.objects.get(pk=category_id)
        # Obtener todos los productos de esa categoría
        productos = Producte.objects.filter(categoria=categoria)
    else:
        # Si no se selecciona una categoría, mostrar todos los productos
        productos = Producte.objects.all()

    # Pasar la categoría al contexto
    return render(request, 'products_category.html', {'categoria': categoria, 'productos': productos})
