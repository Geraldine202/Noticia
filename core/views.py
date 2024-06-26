from urllib import response #¿?¿??
from django.shortcuts import render, redirect
from .models import * 
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .serializers import *
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
import requests
from django.core.paginator import Paginator


def account_locked(request):
    return render(request, 'core/contenido/account_locked.html')

def password_change_form(request):
    return render(request, 'password_change_form.html')


#METODOS PARA LISTAR DESDE EL API
#API
def periodistasapi (request):
    response = requests.get('https://noticia-black.vercel.app/api/periodistas/') 
    periodistas = response.json() 

    paginator = Paginator(periodistas,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    
    aux = {
        'page_obj' : page_obj
    }
    return render (request,'core/crudapi/index.html', aux)


def periodistadetalle(request, id):
    response = requests.get(f'https://noticia-black.vercel.app/api/periodistas/{id}/') 
    periodista = response.json() 

    return render (request,'core/crudapi/detalle.html', {'periodista' : periodista})

#UTILIZAMOS LOS VIEWSET PARA MANEJAR LAS PETICIONES HTTP (GET,POST,PUT,DELETE)
class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = categoriaSerializers
    renderer_classes =[JSONRenderer]

class NoticiaViewset(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = noticiaSerializers
    renderer_classes =[JSONRenderer]

class PeriodistaViewset(viewsets.ModelViewSet):
    queryset = Periodista.objects.all()
    serializer_class = periodistaSerializers
    renderer_classes =[JSONRenderer]

# Create your views here.
def index (request):
    periodistas = Periodista.objects.all() # SELECT * FROM empleado
    response = requests.get('https://api.boostr.cl/feriados/en.json') 
    response2 = requests.get('https://www.mindicador.cl/api/uf') 
    dias_feriados= response.json() 
    plata= response2.json() 

    aux = {              
        'lista' : periodistas,
        'dias_feriados': dias_feriados['data'],
        'moneda' : plata
    }

    return render(request, 'core/index.html', aux)

def register (request):
    aux = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if  formulario.is_valid():
            user = formulario.save()
            #ASIGNAR GRUPO AL USUARIO
            group = Group.objects.get(name='Usuario')
            user.groups.add(group)

            #MENSAJE
            messages.success(request, 'Usuario Creado Correctamente!')
            #aux['msj'] = 'Noticia Almacenada'
            user = authenticate(request=request,username= formulario.cleaned_data['username'] ,password=formulario.cleaned_data['password1'])
            login(request, user)

            #REDIRECCIONA
            return redirect(to="index")
        else:
            aux['form'] = formulario
            

    return render(request, 'registration/register.html',aux)

@permission_required('core.view_noticia')
def noticias (request):
    noticias = Noticia.objects.all().order_by('tipo') # SELECT * FROM empleado
    periodistas = Periodista.objects.all()
    aux = {
        'lista' : noticias,
        'lista2' : periodistas

    }
    return render(request, 'core/noticias/index.html', aux)


@login_required
def cultura (request):
    noticias = Noticia.objects.all() # SELECT * FROM empleado
    periodistass = Periodista.objects.all()
    aux = {
        'lista': noticias,
        'listafiltrada': periodistass

    }
    return render(request, 'core/contenido/cultura.html', aux)


@login_required
def deportes (request):
    noticias = Noticia.objects.all() # SELECT * FROM empleado
    periodistass = Periodista.objects.all()
    aux = {
        'lista': noticias,
        'listafiltrada': periodistass

    }
    return render(request, 'core/contenido/deportes.html',aux)
@login_required
def internacional (request):
    noticias = Noticia.objects.all() # SELECT * FROM empleado
    periodistass = Periodista.objects.all()
    aux = {
        'lista': noticias,
        'listafiltrada': periodistass

    }
    return render(request, 'core/contenido/internacional.html',aux)
@login_required
def economia (request):
    noticias = Noticia.objects.all() # SELECT * FROM empleado
    periodistass = Periodista.objects.all()
    aux = {
        'lista': noticias,
        'listafiltrada': periodistass

    }
    return render(request, 'core/contenido/economia.html',aux)

@login_required
def servicios (request):
    noticias = Noticia.objects.all() # SELECT * FROM empleado
    periodistass = Periodista.objects.all()
    aux = {
        'lista': noticias,
        'listafiltrada': periodistass

    }
    return render(request, 'core/contenido/servicios.html', aux)


@login_required
def contacto (request):
    return render(request, 'core/nav/contacto.html')

@login_required
def voucher (request):
    return render(request, 'core/contenido/voucher.html')

@login_required
def solicitud (request):
    noticias = Noticia.objects.all().order_by('estado') # SELECT * FROM empleado
    periodistas = Periodista.objects.all()
    aux = {
        'lista' : noticias,
        'lista2' : periodistas

    }
    
    return render(request, 'core/nav/solicitud.html',aux)

@permission_required('core.change_noticia')
def soliupdate (request, id):

    noticia = Noticia.objects.get(id=id) #buscador
    aux = {
        'form' : NoticiaClienteForm(instance=noticia)
    }

    if request.method == 'POST':
        formulario = NoticiaClienteForm(data=request.POST,instance=noticia, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, 'Noticia Modificada!')
            return redirect('solicitud')
        else:
            aux['form'] = formulario
            messages.error(request, 'No se pudo modificar')

    return render(request, 'core/nav/soliciupdate.html',aux)

@permission_required('core.add_noticia')
def solicsadd (request):
    aux = {
        'form' : NoticiasoladdForm()
    }
    if request.method == 'POST':
        formulario = NoticiasoladdForm(request.POST, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, 'Noticia enviada con Exito!')
        else:
            aux['form'] = formulario
            messages.error(request, 'No se pudo enviar la noticia!')
    return render(request, 'core/nav/solisadd.html',aux)


@login_required
def galeria (request):
    noticias = Noticia.objects.all() # SELECT * FROM empleado
    aux = {
        'lista': noticias,
    }
    return render(request, 'core/nav/galeria.html',aux)

@login_required
def monja (request):
    return render(request, 'core/contenido/monja.html')

@permission_required('core.add_noticia')
def noticiasadd (request):
    aux = {
        'form' : NoticiaForm()
    }
    if request.method == 'POST':
        formulario = NoticiaForm(request.POST, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, 'Noticia Agregada Correctamente!')
        else:
            aux['form'] = formulario
            messages.error(request, 'No se pudo almacenar la noticia!')
    return render(request, 'core/noticias/crud/add.html',aux)

@permission_required('core.change_noticia')
def noticiasupdate (request, id):
    noticia = Noticia.objects.get(id=id) #buscador
    aux = {
        'form' : NoticiaForm(instance=noticia)
    }

    if request.method == 'POST':
        formulario = NoticiaForm(data=request.POST,instance=noticia, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, 'Noticia Modificada!')
        else:
            aux['form'] = formulario
            messages.error(request, 'No se pudo modificar')

    return render(request, 'core/noticias/crud/update.html',aux)

@permission_required('core.delete_noticia')
def noticiasdelete(request,id):
    noticia = Noticia.objects.get(id=id) #buscador
    noticia.delete()

    return redirect(to="noticias")

#Periodista
@permission_required('core.view_periodista')
def periodistas (request):
    periodistas = Periodista.objects.all() # SELECT * FROM empleado

    paginator = Paginator(periodistas,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    aux = {
        'page_obj' : page_obj

    }
    return render(request, 'core/periodistas/index.html', aux)


@permission_required('core.add_periodista')
def periodistasadd (request):
    aux = {
        'form' : PeriodistaForm()
    }
    if request.method == 'POST':
        formulario = PeriodistaForm(request.POST, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, 'Periodista Agregado Correctamente!')
        else:
            aux['form'] = formulario
            messages.error(request, 'Periodista No Agregado!')
    return render(request, 'core/periodistas/crud/add.html',aux)

@permission_required('core.change_periodista')
def periodistasupdate (request, id):
    periodista = Periodista.objects.get(id=id) #buscador
    aux = {
        'form' : PeriodistaForm(instance=periodista)
    }

    if request.method == 'POST':
        formulario = PeriodistaForm(data=request.POST,instance=periodista, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, 'Periodista Modificado!')
        else:
            aux['form'] = formulario
            messages.error(request, 'Periodista NO Modificado!')


    return render(request, 'core/periodistas/crud/update.html',aux)

@permission_required('core.delete_periodista')
def periodistasdelete(request,id):
    periodista = Periodista.objects.get(id=id) #buscador
    periodista.delete()

    return redirect(to="periodistas")


#EMPLEADOS API
#paginator = Paginator(algo,5) #CANTIDAD DE DATOS A MOSTRAR
#page_number = request.GET.get('page')
#page_obj = paginator.get_page(page_number)
