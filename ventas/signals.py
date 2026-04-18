from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pedido
import logging

# Registrar errores
logger = logging.getLogger(__name__)

# cuando guardamos un pedido restamos stock
@receiver(post_save, sender=Pedido)
def restar_stock_al_confirmar(sender, instance, **kwargs):
    # Verificamos si el pedido ha pasado a estado CONFIRMADO
    if instance.estado.codigo == 'CONFIRMADO':
        for linea in instance.lineas.all():
            producto = linea.producto
            if producto.stock >= linea.cantidad:
                producto.stock -= linea.cantidad
                producto.save()
            else:
                logger.error(f"Error: Stock insuficiente para {producto.nombre} en el Pedido {instance.id}")