import random
from django_seed import Seed
from .sistema_logistica_app.models import Client, Recipient, Package, Form, FormItem, StatesEnum
from django.utils import timezone
from datetime import timedelta

seeder = Seed.seeder()

# Genera clientes aleatorios
seeder.add_entity(Client, 20)

# Genera destinatarios aleatorios
seeder.add_entity(Recipient, 20)

# Genera paquetes y asócialos a clientes, destinatarios y estados aleatorios
def generate_package_data():
    return {
        'recipient': random.choice(Recipient.objects.all()),
        'weight': round(random.uniform(0.1, 10), 2),
        'height': round(random.uniform(10, 100), 2),
        'state': random.choice([state.value for state in StatesEnum]),
        'client': random.choice(Client.objects.all()),
    }

seeder.add_entity(Package, 15, generate_package_data)

# Genera formularios con paquetes asociados
def generate_form_data():
    return {
        'date': timezone.now() - timedelta(days=random.randint(1, 30)),
    }

def generate_form_item_data(form):
    return {
        'package': random.choice(Package.objects.all()),
        'form': form,
        'position': random.randint(1, 10),
        'failureReason': None,  # Opcional: Cambia a un valor de FailureReason si deseas
    }

seeder.add_entity(Form, 3, generate_form_data)
seeder.add_entity(FormItem, 15, generate_form_item_data)

# Ejecuta la generación de datos
inserted_pks = seeder.execute()

print(f"Datos de prueba generados: {inserted_pks}")
