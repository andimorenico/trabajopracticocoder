from django.shortcuts import render, redirect
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm, ContactoForm  # Importan formularios

# Vista principal - FALTABA ESTA FUNCIÓN
def index(request):
    return render(request, 'entrega3/index.html')

# Vista existente para productos
def productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'entrega3/productos.html', context)

# Nueva vista para crear producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda automáticamente en la base de datos
            return redirect('productos')  # Redirige a la lista de productos
    else:
        form = ProductoForm()
    
    context = {'form': form}
    return render(request, 'entrega3/crear_producto.html', context)

# Vista para mostrar clientes - FALTABA ESTA FUNCIÓN
def clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'entrega3/clientes.html', context)

# Vista para crear cliente
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    
    context = {'form': form}
    return render(request, 'entrega3/crear_cliente.html', context)

# Vista para formulario de contacto
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesar datos del formulario
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            # Aquí podrías enviar email, guardar en BD, etc.
            return render(request, 'entrega3/contacto_exitoso.html')
    else:
        form = ContactoForm()
    
    context = {'form': form}
    return render(request, 'entrega3/contacto.html', context)