from django import forms

class ClienteFormulario(forms.Form):

       nombre = forms.CharField()
       apellido = forms.CharField()
       mail = forms.EmailField()
       usuario = forms.CharField()

class BusquedaFormulario(forms.Form):

       album = forms.CharField()
       artista = forms.CharField()
       año = forms.IntegerField()


class AgregarAlbum(forms.Form):

       album = forms.CharField()
       artista = forms.CharField()
       fechaLanzamiento = forms.IntegerField()
       genero = forms.CharField()
       subGenero = forms.CharField()
       formato = forms.CharField()
       paisOrigen = forms.CharField()
       disponibilidad = forms.BooleanField()
       codigo = forms.IntegerField()
       descripcion = forms.CharField()

class Suscripcion(forms.Form):

       mail = forms.EmailField()
       nombre = forms.CharField()
