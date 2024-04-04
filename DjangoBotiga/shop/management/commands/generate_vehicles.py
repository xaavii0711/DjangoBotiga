# En tu_app/management/commands/generate_vehicles.py

import json
from faker import Faker
from django.core.management.base import BaseCommand
from shop.models import Categoria, Tag, Producte  # Reemplaza `tu_app` con el nombre de tu app
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)

class Command(BaseCommand):
    help = 'Genera vehículos aleatorios'

    def add_arguments(self, parser):
        parser.add_argument('cantidad', type=int, help='Número de vehículos a crear')

    def handle(self, *args, **options):
        cantidad = options['cantidad']

        for _ in range(cantidad):
            # Generar datos aleatorios del vehículo
            make_model = fake.vehicle_make_model()
            year = fake.vehicle_year()
            category = fake.vehicle_category()

            # Obtener o crear la categoría del vehículo
            categoria, _ = Categoria.objects.get_or_create(nom=category)

            # Crear un registro de producto en la base de datos
            producte = Producte.objects.create(
                nom=f"{year} {make_model}",
                descripcio=fake.text(),
                preu=fake.random_number(digits=5),
                categoria=categoria,  # Asignar la categoría del vehículo
                quantitat_disponible=fake.random_number(digits=2)
            )

            # Generar tags aleatorios para el producto (opcional)
            num_tags = fake.random_number(digits=1)
            tags = Tag.objects.order_by('?')[:num_tags]
            producte.tags.add(*tags)

            self.stdout.write(self.style.SUCCESS(f'Se ha creado un vehículo: {year} {make_model} en la categoría: {category}'))
