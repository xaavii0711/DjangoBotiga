# En tu_app/management/commands/generate_users.py

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from shop.models import Compra, DetallCompra, Producte
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Genera usuarios y asociaciones a compras'

    def add_arguments(self, parser):
        parser.add_argument('cantidad', type=int, help='Número de usuarios a crear')

    def handle(self, *args, **options):
        cantidad = options['cantidad']

        for _ in range(cantidad):
            # Generar datos aleatorios del usuario
            username = fake.user_name()
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()

            # Crear un usuario en la base de datos
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email)

            # Crear una nueva compra para el usuario
            compra = Compra.objects.create(usuari=user, preu_total=0)  # Inicializar el total de la compra en 0
            
            total_compra = 0  # Inicializar el total de la compra

            # Agregar productos a la compra
            num_productos = fake.random_number(digits=1)
            for _ in range(num_productos):
                producte = Producte.objects.order_by('?').first()
                quantitat = fake.random_number(digits=1)
                preu_unitari = producte.preu
                DetallCompra.objects.create(producte=producte, compra=compra, quantitat=quantitat, preu_unitari=preu_unitari)
                
                total_compra += quantitat * preu_unitari  # Actualizar el total de la compra

            # Actualizar el total de la compra en el objeto Compra
            compra.preu_total = total_compra
            compra.save()

            self.stdout.write(self.style.SUCCESS(f'Se ha creado el usuario: {username} ({first_name} {last_name}) con {num_productos} productos en su compra con un total de {total_compra}'))
