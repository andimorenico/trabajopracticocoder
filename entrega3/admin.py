from django.contrib import admin
from .models import Producto, Cliente, Pedido

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'activo']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'fecha_registro']
    search_fields = ['nombre', 'apellido', 'email']

admin.site.register(Pedido)
