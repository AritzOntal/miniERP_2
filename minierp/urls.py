from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ventas.views import ProductoViewSet

# este es el que me lleva al ProductoViewSet (donde esta la autenticacion, etc...)

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # Esto crea ruta de productos 
    path('api/', include(router.urls)),
]
