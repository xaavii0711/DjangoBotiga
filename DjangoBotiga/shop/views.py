from django.shortcuts import render, HttpResponse, redirect
from .models import *

def product_list(request):
    categorias = Categoria.objects.all()
    productos = Producte.objects.all()
    return render(request, 'product_list.html', {
        'categorias': categorias,
        'productos': productos
        })

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


def carrito(request):
    # Aquí puedes añadir la lógica para obtener los productos del carrito si es necesario
    # Por ejemplo, obtener los productos almacenados en la sesión o base de datos
    # products_in_cart = ...

    # Pasa los productos al contexto si es necesario
    # context = {'products': products_in_cart}

    return render(request, 'shopping_cart.html')  # Renderiza el template del carrito

def add_to_cart(request, product_id):
    # Aquí puedes implementar la lógica para agregar el producto al carrito
    # Por ejemplo, almacenarlo en la sesión
    if 'cart' not in request.session:
        request.session['cart'] = []

    request.session['cart'].append(product_id)
    request.session.modified = True

    return redirect('carrito')