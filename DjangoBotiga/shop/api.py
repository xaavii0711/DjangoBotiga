from django.http import JsonResponse
from shop.models import *
    
#...
    
def getProducts(request):
    jsonData = list( Producte.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "productes": jsonData,
        }, safe=False)


def getProductsByCategory(request, category_id):
    jsonData = list( Producte.objects.filter(categoria = category_id).values() )
    return JsonResponse({
            "status": "OK",
            "productes": jsonData,
        }, safe=False)
