from django.contrib import admin
from .models import *   # import all models from models.py

# admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Tienda)
admin.site.register(Descuento)
admin.site.register(ReseñaxTienda)
admin.site.register(ReseñaProducto)
admin.site.register(EventoxTienda)
admin.site.register(TiendaxProveedor)
admin.site.register(Perfil)

# Register your models here.
