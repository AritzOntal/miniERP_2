from django.db import models
from django.core.validators import MinValueValidator

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    nif = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        # Si el cliente tiene un email guardado, mostramos ambos
        if self.email:
            return f"{self.nombre} - {self.email}"
        # Si no tiene email, mostramos solo el nombre para evitar el "None"
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    sku = models.CharField(max_length=50, unique=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=5, decimal_places=2, default=21.00)
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"[{self.sku}] {self.nombre} - Stock: {self.stock}"

class Estado(models.Model):
    ESTADOS_CHOICES = [
        ('BORRADOR', 'Borrador'),
        ('CONFIRMADO', 'Confirmado'),
        ('FACTURADO', 'Facturado'),
        ('COBRADO', 'Cobrado'),
    ]
    codigo = models.CharField(max_length=20, unique=True, choices=ESTADOS_CHOICES)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Estados de Pedido"

    def __str__(self):
        return self.descripcion 