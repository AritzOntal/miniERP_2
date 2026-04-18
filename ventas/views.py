from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core.models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    #Esta es la consulta
    queryset = Producto.objects.all()
    #usa la clase para serializar y poder enciviar los datos al navegador
    serializer_class = ProductoSerializer

    #bloqueo a usuarios no autenticados
    permission_classes = [IsAuthenticated]
