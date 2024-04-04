from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    nom = models.CharField(max_length=100)
    descripcio = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Producte(models.Model):
    nom = models.CharField(max_length=200)
    descripcio = models.TextField()
    preu = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
    quantitat_disponible = models.IntegerField(default=0)
    def __str__(self):
        return self.nom

class Cistella(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    producte = models.ManyToManyField(Producte)
    quantitat = models.IntegerField(default=1)

class Compra(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    productes = models.ManyToManyField(Producte, through='DetallCompra')
    data_compra = models.DateTimeField(auto_now_add=True)
    preu_total = models.DecimalField(max_digits=10, decimal_places=2)

class DetallCompra(models.Model):
    producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    quantitat = models.IntegerField(default=1)
    preu_unitari = models.DecimalField(max_digits=10, decimal_places=2)