# -*- encoding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from gediapp.models import *
from django.contrib.auth.models import User
import time


class IntegranteForm(ModelForm):
    class Meta:
        model = Integrante
        fields = ['nombres', 'apellidos', 'horas_dedicacion',
                  'fecha_inicio_vin', 'fecha_fin_vin', 'actual']

        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba aquí sus nombres...'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba aquí sus apellidos...'}),
            'horas_dedicacion': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'value': '0'}),
            'fecha_inicio_vin': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_fin_vin': forms.DateInput(attrs={'class': 'form-control','disabled':''}),
            'actual' : forms.CheckboxInput(attrs={'type':'checkbox', 'class':'js-switch_2 js-check-change'}),
        }

class UserForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['foto']


class ArticuloForm(ModelForm):

    class Meta:
        model = Articulo
        fields = ['autores', 'tipo_articulo', 'titulo_articulo', 'pagina_inicial', 'pagina_final', 'idioma', 'anio', 'mes',
                  'revista', 'volumen', 'fasciculo', 'serie_revista', 'pais', 'ciudad', 'medio_divulgacion', 'sitio_web', 'DOI']

        widgets = {
            'autores': forms.SelectMultiple(attrs={'class': 'form-control chosen-select', 'data-placeholder': 'Seleccione un autor...', 'multiple':1, 'tabindex':'4'}),
            'tipo_articulo': forms.Select(attrs={'class': 'form-control chosen-select', 'data-placeholder': 'Seleccione un tipo...'}),
            'titulo_articulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título...'}),
            'pagina_inicial': forms.NumberInput(attrs={'class': 'form-control', 'value':'0', 'min': '0'}),
            'pagina_final': forms.NumberInput(attrs={'class': 'form-control', 'value':'0', 'min': '0'}),
            'idioma':  forms.TextInput(attrs={'class': 'form-control', 'data-placeholder': 'Seleccione un idioma...'}), #Para probar si funciona mientras se implementa el choices de idioma desde el html
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'min': '1950', 'max': '2015'}),
            'mes': forms.Select(attrs={'class': 'form-control chosen-select'}),
            'revista': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la revista...'}),
            'volumen': forms.NumberInput(attrs={'class': 'form-control', 'value':'0', 'min': '0'}),
            'fasciculo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fascículo de la revista...'}),
            'serie_revista': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serie revista...'}),
            'pais': forms.TextInput(attrs={'class': 'form-control '}), #Para probar si funciona mientras se implementa el choices de pais desde el html
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad...'}),
            'medio_divulgacion': forms.Select(attrs={'class': 'form-control chosen-select'}),
            'sitio_web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL...'}),
            'DOI': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DOI...'}),
        }


class SoftwareForm(ModelForm):

    class Meta:
        model = Softwares
        fields = ['tipo', 'nombre', 'pais', 'year', 'disponibilidad', 'web',
                  'nombre_comercial', 'nombre_proyecto', 'institucion_financiadora','descripcion' ,'autores']

        widgets = {
            'tipo':
            forms.Select(attrs={'class': 'form-control m-b'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba el nombre del software aqui...'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': '1950', 'value': '2015'}),
            'disponibilidad': forms.Select(attrs={'class': 'form-control m-b'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo.com'}),
            'nombre_comercial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre comercial del producto...'}),
            'nombre_proyecto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proyecto...'}),
            'institucion_financiadora': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institucion financiadora del proyecto...'}),
            'autores': forms.SelectMultiple(attrs={'data-placeholder': 'Elija los autores...', 'class': 'form-control chosen-select', 'multiple': '',  'tabindex': '4'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','placeholder': 'Una pequeña descripcion...'}),
        }


class TrabajoDirigidoForm(ModelForm):

    class Meta:
        model = TrabajosDirigidos
        fields = ['tipo', 'nombre', 'fecha_inicio', 'fecha_fin', 'tipo_orientacion', 'nombre_estudiante',
                  'programa_academico', 'numero_paginas', 'valoracion', 'institucion', 'autores', 'director']

        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control m-b'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del trabajo dirigido...'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'value': str(time.strftime("%m/%d/%Y"))}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'value': str(time.strftime("%m/%d/%Y"))}),
            'tipo_orientacion': forms.Select(attrs={'class': 'form-control m-b'}),
            'nombre_estudiante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del estudiante...'}),
            'programa_academico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del programa...'}),
            'numero_paginas': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'value': '0'}),
            'valoracion': forms.Select(attrs={'class': 'form-control m-b'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.SelectMultiple(attrs={'data-placeholder': 'Elija los autores...', 'class': 'form-control chosen-select', 'multiple': '',  'tabindex': '4'}),
            'director': forms.TextInput(attrs={'data-placeholder': 'Seleccione un director...', 'class': 'form-control'}),
        }

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña', 'required':1}))

    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de usuario', 'required':1})
        }


class LibroForm(ModelForm):

    class Meta:
        model = Libro
        fields = ['autores', 'titulo_libro','pais','ciudad','anio','mes','idioma','ISBN','volumen', 'paginas', 'editorial']

        widgets = {
            'autores': forms.SelectMultiple(attrs={'class': 'form-control chosen-select', 'data-placeholder': 'Seleccione un autor...', 'multiple':1, 'tabindex':'4'}),
            'titulo_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título...'}),
            'pais': forms.TextInput(attrs={'class': 'form-control '}), #Para probar si funciona mientras se implementa el choices de pais desde el html
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad...'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'min': '1950', 'max': '2015'}),
            'mes': forms.Select(attrs={'class': 'form-control chosen-select'}),
            'idioma':  forms.TextInput(attrs={'class': 'form-control', 'data-placeholder': 'Seleccione un idioma...'}), #Para probar si funciona mientras se implementa el choices de idioma desde el html
            'ISBN': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN...'}),
            'volumen': forms.NumberInput(attrs={'class': 'form-control', 'value':'0', 'min': '0'}),
            'paginas': forms.NumberInput(attrs={'class': 'form-control', 'value':'0', 'min': '0'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Editorial...'})
        }

class CapituloLibroForm(forms.ModelForm):

   class Meta:
        model = CapitulosLibros
        fields = ['autores', 'titulo_capitulo_libro', 'titulo_libro', 'ISBN_libro', 'anio_presentacion', 'mes_presentacion']

        widgets = {
            'autores': forms.SelectMultiple(attrs={'class': 'form-control chosen-select', 'data-placeholder': 'Seleccione un integrante...', 'multiple':1, 'tabindex':'4'}),
            'titulo_capitulo_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del capitulo del libro...'}),
            'titulo_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del libro...'}),
            'ISBN_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN del libro...'}),
            'anio_presentacion': forms.NumberInput(attrs={'class': 'form-control', 'min': '1950', 'max': '2015'}),
            'mes_presentacion': forms.Select(attrs={'class': 'form-control chosen-select'}),

        }


class PicForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = '__all__' 

class CropForm(forms.Form):
    """Django form for accepting the information passed after cropping a loaded 
    image
    """
    imgUrl = forms.CharField() # your image path (the one we received after successful upload)
    imgInitW = forms.DecimalField()          # your image original width (the one we received after upload)
    imgInitH = forms.DecimalField()          # your image original height (the one we received after upload)
    imgW = forms.DecimalField()              # your new scaled image width
    imgH = forms.DecimalField()              # your new scaled image height
    imgX1 = forms.DecimalField()             # top left corner of the cropped image in relation to scaled image
    imgY1 = forms.DecimalField()             # top left corner of the cropped image in relation to scaled image
    cropW = forms.DecimalField()             # cropped image width
    cropH = forms.DecimalField()             # cropped image height

class NoticiaForm(ModelForm):

    class Meta:
        model = Noticias
        fields = [ 'titulo_noticia','descripcion','fecha_inicio','fecha_fin']

        widgets = {
            'titulo_noticia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título...'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control '}), #Para probar si funciona mientras se implementa el choices de pais desde el html
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control'})
        }