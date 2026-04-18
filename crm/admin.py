from django.contrib import admin
from .models import Oportunidad

@admin.register(Oportunidad)
class OportunidadAdmin(admin.ModelAdmin):
    # Columnas
    list_display = ('titulo', 'cliente', 'valor_estimado', 'etapa', 'dias_abierta')
    # Filtro por etapa
    list_filter = ('etapa',)
    # Buscador por título y nombre
    search_fields = ('titulo', 'cliente__nombre')
