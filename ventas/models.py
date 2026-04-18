from django.db import models
from core.models import Cliente, Producto, Estado
from decimal import Decimal

class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT, related_name='pedidos')
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT)

    def __str__(self):
        return f"Pedido {self.id} - Cliente {self.cliente.nombre} - Estado: {self.estado.descripcion} - Total: {self.total} €" 

# metodo de cálculo
    def calcular_totales(self):
        # Sumamos y con consulta SELECT (ya tiene los datos por que ya se guardo antes)
        base = sum(linea.cantidad * linea.precio_aplicado for linea in self.lineas.all())
        
        # Convertimos todo a Decimal para evitar errores de precisión
        base_decimal = Decimal(str(base))
        iva = base_decimal * Decimal('0.21')
        
        # Guardamos el total
        self.total = base_decimal + iva
        # ejecuta UPDATE para guardar permanentemente el cálculo
        self.save()

class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='lineas') 
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT) 
    cantidad = models.IntegerField()
    precio_aplicado = models.DecimalField(max_digits=10, decimal_places=2) 

    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(cantidad__gt=0), name='cantidad_positiva_linea')
        ]

    def __str__(self):
        return f"Línea de pedido {self.pedido.id} - {self.producto.nombre}"

    def save(self, *args, **kwargs):
        # Primero guardamos la línea de pedido en la base de datos
        super().save(*args, **kwargs)
        # accede a la clave foranea (Pedido) para disparar el metodo calcular_totales
        self.pedido.calcular_totales()