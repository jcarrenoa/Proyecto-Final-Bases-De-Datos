from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import logout
from myapp.models import *
from django.views.decorators.csrf import csrf_exempt

def login(request):
    return render(request, 'lr/sesion.html', {'title': 'Inicio de sesion'})
    
# Create your views here.
def index(request):
    tiendas = Tienda.objects.all()
    return render(request, 'app/index.html', {'tiendas': tiendas, 'title': 'Inicio'})

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            if request.POST['password1'] == request.POST['password2']:    
                form.save() 
                messages.success(request, 'Cuenta creada exitosamente')
                return redirect('login')
            else:
                messages.error(request, 'Las contraseñas no coinciden')
                return render(request, 'lr/registro.html', {'title': 'Registro'})
        else:
            messages.error(request, 'Algun campo no cumple con los requisitos')
            return redirect('register')
    else:
        form = RegistroForm()
    context = {'form': form}
    return render(request, 'lr/registro.html', context)

def exit(request):
    logout(request)
    return redirect('index')

def tienda(request, idTienda):
    tiendas = Tienda.objects.values()
    tienda_n = Tienda.objects.filter(idTienda=idTienda).values()[0]
    productos = Producto.objects.filter(idTienda=idTienda).all()
    Reseñas = ReseñaxTienda.objects.filter(idTienda=idTienda, Puntuacion=5).all()
    print(productos)
    print(Reseñas)
    categorias = Categoria.objects.values()
    return render(request, 'app/tienda.html', {'tiendas': tiendas, 'tienda_n': tienda_n, 'productos': productos, 'isnull': Producto.objects.filter(idTienda=idTienda).all().count() == 0, 
                                               'idTienda': idTienda, 'Reseñas': Reseñas, 'categorias': categorias, 'title': 'Tienda'})

def proveedores(request, idTienda):
    proveedores = Proveedor.objects.filter(idTienda=idTienda).all()
    return render(request, 'app/proveedores.html', {'proveedores': proveedores, 'isnull': Proveedor.objects.filter(idTienda=idTienda).all().count() == 0, 'idTienda': idTienda})

def descuentos(request, idTienda):
    tiendas = Tienda.objects.values()
    tienda_n = Tienda.objects.filter(idTienda=idTienda).values()[0]
    descuentos = Descuento.objects.filter(idTienda=idTienda).all()
    print(descuentos)
    print(tiendas)
    return render(request, 'app/descuentos.html', {'descuentos': descuentos, 'isnull': Descuento.objects.filter(idTienda=idTienda).all().count() == 0, 
                                                    'idTienda': idTienda, 'tienda_n': tienda_n, 'tiendas': tiendas, 'title': 'Descuentos'})

def eventos(request, idTienda):
    tiendas = Tienda.objects.values()
    tienda_n = Tienda.objects.filter(idTienda=idTienda).values()[0]
    eventos = EventoxTienda.objects.filter(idTienda=idTienda).all()
    return render(request, 'app/eventos.html', {'eventos': eventos, 'isnull': EventoxTienda.objects.filter(idTienda=idTienda).all().count() == 0, 
                                                'idTienda': idTienda, 'tienda_n': tienda_n, 'tiendas': tiendas, 'title': 'Eventos'})
 
