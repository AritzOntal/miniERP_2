from django.contrib import admin
from .models import Cliente, Producto, Estado

# Usamos el decorador y personalizamos la vista del Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'nif')
    search_fields = ('nombre', 'email', 'nif')

admin.site.register(Producto)
admin.site.register(Estado) 