from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('crear-producto/', views.crear_producto, name='crear_producto'),
    path('clientes/', views.clientes, name='clientes'),
    path('crear-cliente/', views.crear_cliente, name='crear_cliente'),
    path('contacto/', views.contacto, name='contacto'),
]