from django.contrib import admin
from .models import Pedido, LineaPedido

# Vista para añadir lineas
class LineaPedidoInline(admin.TabularInline):
    model = LineaPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    # Metemos aquí el inline creado antes
    inlines = [LineaPedidoInline]
    list_display = ('id', 'cliente', 'estado', 'fecha_pedido', 'total')
    list_filter = ('estado', 'fecha_pedido')

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(LineaPedido)