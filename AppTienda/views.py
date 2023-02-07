from django.shortcuts import render
from django.http import HttpResponse
from AppTienda.models import *
from AppTienda.forms import *

def inicio(request):
      return render(request, 'AppTienda/inicio.html')

def tienda(request):

      return render(request, 'AppTienda/tienda.html')
 
def cliente(request):
      return render(request, 'AppTienda/cliente.html')
      
def contacto(request):
      return render(request, 'AppTienda/contacto.html')

def cotizar(request):
      return render(request, 'AppTienda/cotizar.html')

def suscribete(request):
      return render(request, 'AppTienda/suscribete.html')

def preventa(request):
      return render(request, 'AppTienda/preventa.html')




def clienteFormulario(request):    

      if request.method == 'POST':
            formulario1 = ClienteFormulario(request.POST)
            if formulario1.is_valid():
                  info = formulario1.cleaned_data

                  cliente = Cliente(nombre=info['nombre'], apellido=info['apellido'], mail=info['mail'], usuario=info['usuario'])
                  
                  cliente.save()
                  return render(request, 'Apptienda/inicio.html')

      else:

                  formulario1 = ClienteFormulario()

      return render(request, 'AppTienda/clienteFormulario.html', {"form1":formulario1})

def busquedaCliente(request): #PAGINA PARA BUSCAR

      return render(request, 'AppTienda/inicio.html')

def resultadoCliente(request): #RESULTADOS

      if request.GET['nombre']:

            nombre = request.GET['nombre']
            usuario = Cliente.objects.filter(nombre__icontains=nombre)

            return render(request, "AppTienda/inicio.html", {"usuario":usuario, "nombre":nombre})
      else:
            respuesta = "No hay resultados."

      return HttpResponse(respuesta)

def agregarAlbum(request):    

      if request.method == 'POST':
            formulario2 = AgregarAlbum(request.POST)
            if formulario2.is_valid():
                  info = formulario2.cleaned_data

                  cliente = Tienda(album=info['album'], artista=info['artista'], fechaLanzamiento=info['fechaLanzamiento'], genero=info['genero'], subGenero=info['subGenero'], formato=info['formato'], paisOrigen=info['paisOrigen'], disponibilidad=info['disponibilidad'], codigo=info['codigo'])
                  
                  cliente.save()
                  return render(request, 'Apptienda/inicio.html')

      else:

                  formulario2 = AgregarAlbum()

      return render(request, 'AppTienda/agregarAlbum.html', {"form2":formulario2})

def resultadoBusqueda(request): #RESULTADOS

      if request.GET['artista']:

            artista = request.GET['artista']
            album = Tienda.objects.filter(artista__icontains=artista)

            return render(request, "AppTienda/inicio.html", {"album":album, "artista":artista})
      else:
            respuesta = "No hay resultados."

      return HttpResponse(respuesta)

def suscripcion(request):    

      if request.method == 'POST':
            formulario3 = Suscripcion(request.POST)
            if formulario3.is_valid():
                  info = formulario3.cleaned_data

                  client3 = Suscribete(mail=info['mail'], nombre=info['nombre'])
                  
                  client3.save()
                  return render(request, 'Apptienda/inicio.html')

      else:

                  formulario3 = Suscripcion()

      return render(request, 'AppTienda/suscribete.html', {"form3":formulario3})