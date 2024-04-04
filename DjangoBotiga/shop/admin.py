from django.contrib import admin
from .models import *

admin.site.register(Tag)
admin.site.register(Producte)
admin.site.register(DetallCompra)

class ProducteInline(admin.TabularInline):
    model = Producte
    readonly_fields = ["descripcio"]

class CategoriaInline(admin.TabularInline):
    model = Categoria
    extra = 0
    exclude = ("descripcio",)

class DetallInline(admin.TabularInline):
    model = DetallCompra
    readonly_fields = ["producte", "quantitat", "preu_unitari"]
    

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [CategoriaInline, ProducteInline]
    list_display = ['nom','parent']
    
admin.site.register(Categoria, CategoriaAdmin)

class CistellaAdmin(admin.ModelAdmin):
    filter_horizontal = ('producte',)

admin.site.register(Cistella, CistellaAdmin)

class CompraAdmin(admin.ModelAdmin):
    inlines = [DetallInline]
    
admin.site.register(Compra, CompraAdmin)




# Register your models here.
