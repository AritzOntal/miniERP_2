from django.contrib import admin
from .models import Cliente, Producto, Estado
from .forms import ProductoForm, ClienteForm

# Usamos el decorador y personalizamos la vista del Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'nif')
    search_fields = ('nombre', 'email', 'nif')
    #aqui usamos el formulario tuneado con validaciones y stock
    form = ClienteForm


class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Estado) 