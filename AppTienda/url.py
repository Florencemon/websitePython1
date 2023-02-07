
from django.urls import path
from AppTienda.views import *

urlpatterns = [
    path('inicio', inicio, name='inicio'),
    path('tienda', tienda, name='tienda'),
    path('cliente', cliente, name='cliente'),
    path('contacto', contacto, name='contacto'),
    path('cotizar/', cotizar, name='cotizar'),
    path('suscribete/', suscribete, name='suscribete'),
    path('preventa', preventa, name='preventa'),
    path('clienteFormulario/', clienteFormulario, name='clienteFormulario'),
    path('busquedaCliente', busquedaCliente, name="busquedaCliente"),
    path('resultadoCliente/',resultadoCliente, name="resultadoCliente"),
    path('agregarAlbum/',agregarAlbum, name="agregarAlbum"),
    path('resultadoBusqueda/',resultadoBusqueda, name="resultadoBusqueda"),
    path('suscripcion/',suscripcion, name="suscripcion"),

    
]
