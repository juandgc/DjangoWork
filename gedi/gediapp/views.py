# -*- encoding: utf-8 -*-
from django.shortcuts import render
from gediapp.forms import IntegranteForm, SoftwareForm, TrabajoDirigidoForm, ArticuloForm, LoginForm, UserForm, LibroForm, CapituloLibroForm , NoticiaForm, PicForm, CropForm
from django.http import HttpResponse, HttpResponseRedirect  # For tests
from gediapp.models import Integrante, Softwares, Articulo, TrabajosDirigidos, UserProfile, Libro, CapitulosLibros, Noticias
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import os
from django.conf import settings
from .dashboards import Dashboard
import json,datetime


from django.core.files.storage import default_storage

from PIL import Image
from io import BytesIO
import base64
import re
import sys


# Create your views here.
profile = None

def inicio(request):
    global profile
    try:
        profile = UserProfile.objects.get(user_id = request.user.id)
    except UserProfile.DoesNotExist:
        profile = None
    #Se obtienen los valores de los reportes con ayuda de una clase adicional
    reportes = Dashboard()
    integrantres,artculos,productos_sf = reportes.totales() #Cuentas de valores de datos
    int_top,art_top,soft_top,t_dir_top = reportes.top_integrante() #Top integrante
    soft_list = reportes.software_list() #Softwares
    last_sf,next_sf = soft_list[0],soft_list[1]
    trab_list = reportes.trabajos_dir_list() #Trabajos
    last_td,next_td = trab_list[0],trab_list[1]
    total_trabajos_dir = reportes.trabajos_dir_total()
    noticias = Noticias.objects.all()
    ##Jsons
    datos_json = []
    for i in range(1,3):
        fecha =  datetime.date(2015,1,i)
        j = json.dumps({
            'fecha': fecha.strftime('%Y-%m-%d'),
            'nombre' : 'Bananas',
            'valor_uno' : 1000+i,
            'valor_dos' : 250+i,
            'posicion' : 'East'
        }, separators=(',', ': '))
        datos_json.append(j)
        j = json.dumps({
            'fecha': fecha.strftime('%Y-%m-%d'),
            'nombre' : 'Apples',
            'valor_uno' : 1200+i,
            'valor_dos' : 400+i,
            'posicion' : 'East'
        }, separators=(',', ': '))
        datos_json.append(j)
        j = json.dumps({
            'fecha': fecha.strftime('%Y-%m-%d'),
            'nombre' : 'Oranges',
            'valor_uno' : 1150+i,
            'valor_dos' : 200+i,
            'posicion' : 'West'
        }, separators=(',', ': '))
        datos_json.append(j)
    #
    ##Columnas
    tipos_dato = ['string','date','number','number','string']
    valores = ['Fruta','Fecha','Ganancias','Gastos','Lugar']
    json_columnas = []
    for i in range(0,len(tipos_dato)):
        dic = {
            'tipo_dato':tipos_dato[i],
            'valor' : valores[i]
        }
        json_c = json.dumps(dic)
        json_columnas.append(json_c)
    #
    return render(request, 'index.html',
                  {'profile':profile,
                   'noticias':noticias,
                   'num_integ':integrantres,
                   'num_art':artculos,
                   'num_soft':productos_sf,
                   'int_top':int_top,
                   'art_top':art_top,
                   'soft_top':soft_top,
                   't_dir_top':t_dir_top,
                   'last_sf':last_sf,
                   'next_sf':next_sf,
                   'last_td':last_td,
                   'next_td':next_td,
                   'num_trab_dir':total_trabajos_dir,
                   'datos_json':datos_json,
                   'columnas': json_columnas
                   })

@login_required
def subir_foto(request):
    global profile
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            usuario = User.objects.get(pk=request.user.id)
            #Si el usuario ya tiene una foto asignada actualice esa foto, sino creela.
            if UserProfile.objects.filter(user = usuario).exists():
                try:
                    profile = UserProfile.objects.get(user=usuario.pk)
                    os.remove(os.path.join(settings.MEDIA_ROOT, profile.foto.name))
                    profile.foto = request.FILES['foto']
                except Exception as e:
                    print('No se encontro la foto: '+str(e))
                profile.save()
                return HttpResponseRedirect("/")
            else:
                profile = UserProfile(user=usuario, foto=request.FILES['foto'])
                profile.save()
                return HttpResponseRedirect("/")
    return render(request,'subir_foto.html',{'profile':profile})

# Vistas de CRUD INTEGRANTE
@login_required
def crear_integrante(request):
    global profile
    if request.method == 'POST':
        form = IntegranteForm(request.POST)
        if form.is_valid():
            integrante  = form.save(commit = False)
            integrante.nombres = integrante.nombres.upper()
            integrante.apellidos = integrante.apellidos.upper()
            integrante.save()
            return render(request, 'crear_integrante.html', {'form': IntegranteForm(), 'exito': True,'profile':profile})
    else:
        form = IntegranteForm()
    return render(request, 'crear_integrante.html', {'form': form, 'exito': False, 'profile':profile})

@login_required
def activacion_integrante(request, id_integrante):
    integ = Integrante.objects.get(pk=id_integrante)
    if integ.activo:
        integ.activo = False
    else:
        integ.activo = True
    integ.save()
    return HttpResponseRedirect("/integrante/listar/")

@login_required
def editar_integrante(request, id_integrante):
    global profile
    integrantes = Integrante.objects.all()
    for int in integrantes:
        if int.fecha_fin_vin == None:
            int.fecha_fin_vin = 'Actual'
    integ = Integrante.objects.get(pk=id_integrante)
    form_edicion = IntegranteForm(instance=integ, initial=integ.__dict__)
    if request.method == 'POST':
        form_edicion = IntegranteForm(
            request.POST, instance=integ, initial=integ.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                integrante_nuevo = form_edicion.save(commit = False)
                integrante_nuevo.nombres = integrante_nuevo.nombres.upper()
                integrante_nuevo.apellidos = integrante_nuevo.apellidos.upper()
                integrante_nuevo.save()
                return HttpResponseRedirect("/integrante/listar/")
        else:
            return HttpResponseRedirect("/integrante/listar/")
    return render(request, 'mostrar_integrante.html', {'integrantes': integrantes, 'edicion': True, 'form_edicion': form_edicion,'profile':profile})


def mostrar_integrante(request):
    global profile
    if request.user.is_authenticated():
        integrantes = Integrante.objects.all()
    else:
        integrantes = Integrante.objects.filter(activo= True)
    for int in integrantes:
        if int.fecha_fin_vin == None:
            int.fecha_fin_vin = 'Actual'
    return render(request, 'mostrar_integrante.html', {'integrantes': integrantes, 'edicion': False,'profile':profile})


# Vistas de CRUD ARTICULO
@login_required
def crear_articulo(request):
    global profile
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.titulo_articulo = articulo.titulo_articulo.upper()
            articulo.idioma = articulo.idioma.upper()
            articulo.revista = articulo.revista.upper()
            articulo.fasciculo = articulo.fasciculo.upper()
            articulo.serie_revista = articulo.serie_revista.upper()
            articulo.pais = articulo.pais.upper()
            articulo.ciudad = articulo.ciudad.upper()
            articulo.save()
            form.save()
            return render(request, 'crear_articulo.html', {'form': ArticuloForm(), 'exito': True,'profile':profile})
    else:
        form = ArticuloForm()
    return render(request, 'crear_articulo.html', {'form': form, 'exito': False,'profile':profile})


def mostrar_articulo(request):
    global profile
    if request.user.is_authenticated():
        articulos = Articulo.objects.all()
    else:
        articulos = Articulo.objects.filter(activo=True)
    for art in articulos:
        autoresxarticulo = ", ".join([(x.nombres+" "+x.apellidos) for x in art.autores.all()])
        art.lista_autores = autoresxarticulo
    return render(request, 'mostrar_articulo.html', {'articulos': articulos, 'edicion':False, 'profile':profile})


@login_required
def editar_articulo(request, id_articulo):
    global profile
    articulos = Articulo.objects.all()
    for art in articulos:
        autoresxarticulo = ", ".join([x.nombres for x in art.autores.all()])
        art.lista_autores = autoresxarticulo
    articulo_editar = Articulo.objects.get(pk=id_articulo)
    form_edicion = ArticuloForm(instance=articulo_editar, initial=articulo_editar.__dict__)
    if request.method == 'POST':
        form_edicion = ArticuloForm(request.POST, instance=articulo_editar, initial=articulo_editar.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                articulo_nuevo = form_edicion.save(commit=False)
                articulo_nuevo.titulo_articulo = articulo_nuevo.titulo_articulo.upper()
                articulo_nuevo.idioma = articulo_nuevo.idioma.upper()
                articulo_nuevo.revista = articulo_nuevo.revista.upper()
                articulo_nuevo.fasciculo = articulo_nuevo.fasciculo.upper()
                articulo_nuevo.serie_revista = articulo_nuevo.serie_revista.upper()
                articulo_nuevo.pais = articulo_nuevo.pais.upper()
                articulo_nuevo.ciudad = articulo_nuevo.ciudad.upper()
                articulo_nuevo.save()
                form_edicion.save()
                return HttpResponseRedirect("/articulo/listar/")
        else:
            return HttpResponseRedirect("/articulo/listar/")
    return render(request, 'mostrar_articulo.html', {'articulos':articulos, 'edicion':True, 'form_edicion':form_edicion,'profile':profile})


@login_required
def activacion_articulo(request,id_articulo):
    art = Articulo.objects.get(pk=id_articulo)
    if art.activo:
        art.activo = False
    else:
        art.activo = True
    art.save()
    return HttpResponseRedirect("/articulo/listar/")

#Vistas de CRUD SOFTWARE
@login_required
def crear_software(request):
    global profile
    if request.method == 'POST':
        pais = request.POST.get('pais')
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.fields['pais'] = pais
            software = form.save(commit=False)
            software.nombre = software.nombre.upper()
            software.pais = software.pais.upper()
            software.nombre_comercial = software.nombre_comercial.upper()
            software.nombre_proyecto = software.nombre_proyecto.upper()
            software.institucion_financiadora = software.institucion_financiadora.upper()
            software.descripcion = software.descripcion.upper()
            software.save()
            form.save()
            return render(request, 'crear_software.html', {'form': SoftwareForm(), 'exito': True,'profile':profile})
    else:
        form = SoftwareForm()
    return render(request, 'crear_software.html', {'form': form, 'exito': False,'profile':profile})


def mostrar_software(request):
    global profile
    if request.user.is_authenticated():
        software_exixstente = Softwares.objects.all()
    else:
        software_exixstente = Softwares.objects.filter(activo=True)
    for soft in software_exixstente:
        autores = ','.join([(aut.nombres + " " + aut.apellidos) for aut in soft.autores.all()])
        soft.lista_autores = autores

    return render(request, 'mostrar_software.html', {'softwares': software_exixstente,'profile':profile})


@login_required
def activacion_software(request, id_soft):
    software = Softwares.objects.get(pk=id_soft)
    if software.activo:
        software.activo = False
    else:
        software.activo = True
    software.save()
    return HttpResponseRedirect('/software/listar/')


@login_required
def editar_software(request,id_soft):
    global profile
    softwares = Softwares.objects.all()
    for soft in softwares:
        autores = ','.join([(aut.nombres + " " + aut.apellidos) for aut in soft.autores.all()])
        soft.lista_autores = autores
    soft = Softwares.objects.get(pk=id_soft)
    form_edicion = SoftwareForm(instance=soft, initial=soft.__dict__)

    if request.method == 'POST':
        pais = request.POST.get('pais')
        form_edicion.fields['pais'] = pais
        form_edicion = SoftwareForm(request.POST,instance=soft,initial=soft.__dict__)

        if form_edicion.has_changed():
         if form_edicion.is_valid():
            software_nuevo=form_edicion.save(commit=False)
            software_nuevo.nombre = software_nuevo.nombre.upper()
            software_nuevo.pais = software_nuevo.pais.upper()
            software_nuevo.nombre_comercial = software_nuevo.nombre_comercial.upper()
            software_nuevo.nombre_proyecto = software_nuevo.nombre_proyecto.upper()
            software_nuevo.institucion_financiadora = software_nuevo.institucion_financiadora.upper()
            software_nuevo.descripcion = software_nuevo.descripcion.upper()
            software_nuevo.save()
            form_edicion.save()
            return HttpResponseRedirect("/software/listar/")
        else:
            return HttpResponseRedirect("/software/listar/")
    return render(request, 'mostrar_software.html', {'softwares': softwares, 'edicion': True, 'form_edicion': form_edicion,'profile':profile})



# Vistas de CRUD TRABAJO DIRIGIDO
@login_required
def crear_tdirigido(request):
    global profile
    if request.method == 'POST':
        form = TrabajoDirigidoForm(request.POST)
        if form.is_valid():
            t_dir = form.save(commit=False)
            t_dir.nombre = t_dir.nombre.upper()
            t_dir.nombre_estudiante = t_dir.nombre_estudiante.upper()
            t_dir.programa_academico = t_dir.programa_academico.upper()
            t_dir.institucion = t_dir.institucion.upper()
            t_dir.director = t_dir.director.upper()
            t_dir.save()
            form.save()
            return render(request, 'crear_tdirigido.html', {'form': TrabajoDirigidoForm(), 'exito': True,'profile':profile})
    else:
        form = TrabajoDirigidoForm()
    return render(request, 'crear_tdirigido.html', {'form': form, 'exito': False,'profile':profile})


def mostrar_tdirigido(request):
    global profile
    if request.user.is_authenticated():
        trabajos_dirigidos = TrabajosDirigidos.objects.all()
    else:
        trabajos_dirigidos = TrabajosDirigidos.objects.filter(activo=True)
    for tdiri in trabajos_dirigidos:
        autores = ','.join([(aut.nombres + " " + aut.apellidos) for aut in tdiri.autores.all()])
        tdiri.lista_autores = autores
    return render(request,'mostrar_tdirigido.html',{'trabajos_dirigidos':trabajos_dirigidos,'profile':profile})


@login_required
def activacion_tdirigido(request,id_tdigirido):
    tdirigido = TrabajosDirigidos.objects.get(pk=id_tdigirido)
    if tdirigido.activo:
        tdirigido.activo = False
    else:
        tdirigido.activo = True
    tdirigido.save()
    return HttpResponseRedirect('/trabajo_dirigido/listar/')


@login_required
def editar_tdirigido(request,id_tdirigido):
    global profile
    trabajos_dirigidos = TrabajosDirigidos.objects.all()
    for tdiri in trabajos_dirigidos:
        autores = ','.join([(aut.nombres + " " + aut.apellidos) for aut in tdiri.autores.all()])
        tdiri.lista_autores = autores
    tdiri = TrabajosDirigidos.objects.get(pk=id_tdirigido)
    form_edicion = TrabajoDirigidoForm(instance=tdiri, initial=tdiri.__dict__)

    if request.method == 'POST':
        form_edicion = TrabajoDirigidoForm(request.POST,instance=tdiri,initial=tdiri.__dict__)
        if form_edicion.has_changed():
         if form_edicion.is_valid():
            tdir_nuevo = form_edicion.save(commit=False)
            tdir_nuevo.nombre = tdir_nuevo.nombre.upper()
            tdir_nuevo.nombre_estudiante = tdir_nuevo.nombre_estudiante.upper()
            tdir_nuevo.programa_academico = tdir_nuevo.programa_academico.upper()
            tdir_nuevo.institucion = tdir_nuevo.institucion.upper()
            tdir_nuevo.director = tdir_nuevo.director.upper()
            tdir_nuevo.save()
            form_edicion.save()
            return HttpResponseRedirect("/trabajo_dirigido/listar/")
        else:
            return HttpResponseRedirect("/trabajo_dirigido/listar/")
    return render(request, 'mostrar_tdirigido.html', {'trabajos_dirigidos': trabajos_dirigidos, 'edicion': True, 'form_edicion': form_edicion,'profile':profile})

@login_required
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect("/")


def iniciar_sesion(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method =='POST':
            usuario = request.POST.get('username')
            contrasena = request.POST.get('password')

            usuario = authenticate(username=usuario,password=contrasena)

            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    return inicio(request)
                else:
                    return render(request,'login.html',{'error':'Su cuenta se encuentra desactivada','form':LoginForm()})
            else:
                error = "Su correo electrónico o contraseña son invalidos"
                return render(request,'login.html',{'error':error,'form':LoginForm()})
        else:
            return render(request,'login.html',{'error':'','form':LoginForm()})


# Vistas de CRUD CAPITULOS LIBRO
@login_required
def crear_caplibro(request):
    global profile
    if request.method == 'POST':
        form = CapituloLibroForm(request.POST)
        if form.is_valid():
            caplibro= form.save(commit=False)
            caplibro.titulo_capitulo_libro=caplibro.titulo_capitulo_libro.upper()
            caplibro.titulo_libro=caplibro.titulo_libro.upper()
            caplibro.ISBN_libro=caplibro.ISBN_libro.upper()
            form.save()
            return render(request, 'crear_caplibro.html', {'form': CapituloLibroForm(), 'exito': True,'profile':profile})
    else:
        form = CapituloLibroForm()
    return render(request, 'crear_caplibro.html', {'form': form, 'exito': False,'profile':profile})


def mostrar_caplibro(request):
    global profile
    if request.user.is_authenticated():
        capitulos_libros = CapitulosLibros.objects.all()
    else:
        capitulos_libros = CapitulosLibros.objects.filter(activo=True)
    for caplibro in capitulos_libros:
        capslibros = ','.join([(aut.nombres + " " + aut.apellidos) for aut in caplibro.autores.all()])
        caplibro.lista_caplibro = capslibros
    return render(request,'mostrar_caplibro.html',{'capitulos_libros':capitulos_libros,'profile':profile})


@login_required
def editar_caplibro(request,id_caplibro):
    global profile
    capitulos_libros = CapitulosLibros.objects.all()
    for caplibro in capitulos_libros:
        capslibros = ','.join([(aut.nombres + " " + aut.apellidos) for aut in caplibro.autores.all()])
        caplibro.lista_caplibro = capslibros
    caplibro_editar = CapitulosLibros.objects.get(pk=id_caplibro)
    form_edicion = CapituloLibroForm(instance=caplibro_editar, initial=caplibro_editar.__dict__)
    if request.method == 'POST':
        form_edicion = CapituloLibroForm(request.POST, instance=caplibro_editar, initial=caplibro_editar.__dict__)
        if form_edicion.has_changed():
            if form_edicion.is_valid():
                caplibro_nuevo = form_edicion.save(commit=False)
                caplibro_nuevo.titulo_capitulo_libro=caplibro_nuevo.titulo_capitulo_libro.upper()
                caplibro_nuevo.titulo_libro=caplibro_nuevo.titulo_libro.upper()
                caplibro_nuevo.ISBN_libro=caplibro_nuevo.ISBN_libro.upper()
                caplibro_nuevo.save()
                form_edicion.save()
                return HttpResponseRedirect("/capitulo_libro/listar/")
        else:
            return HttpResponseRedirect("/capitulo_libro/listar/")
    return render(request, 'mostrar_caplibro.html', {'capitulos_libros':capitulos_libros, 'edicion':True, 'form_edicion':form_edicion, 'profile':profile})



@login_required
def activacion_caplibro(request,id_caplibro):
    caplibro = CapitulosLibros.objects.get(pk=id_caplibro)
    if caplibro.activo:
        caplibro.activo = False
    else:
        caplibro.activo = True
    caplibro.save()
    return HttpResponseRedirect('/capitulo_libro/listar/')




# Vistas de CRUD LIBRO
@login_required
def crear_libro(request):
    global profile
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro= form.save(commit=False)
            libro.titulo_libro=libro.titulo_libro.upper()
            libro.pais = libro.pais.upper()
            libro.ciudad = libro.ciudad.upper()
            libro.editorial = libro.editorial.upper()
            form.save()
            return render(request, 'crear_libro.html', {'form': LibroForm(), 'exito': True,'profile':profile})
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form, 'exito': False,'profile':profile})


def mostrar_libro(request):
    global profile
    if request.user.is_authenticated():
        libros = Libro.objects.all()
    else:
        libros = Libro.objects.filter(activo=True)
    for lib in libros:
        autoresxlibro = ", ".join([(x.nombres+" "+x.apellidos) for x in lib.autores.all()])
        lib.lista_autores = autoresxlibro
    return render(request, 'mostrar_libro.html', {'libros': libros, 'edicion':False, 'profile':profile})


@login_required
def editar_libro(request, id_libro):
    global profile
    libros = Libro.objects.all()
    for lib in libros:
        autoresxlibro = ", ".join([x.nombres for x in lib.autores.all()])
        lib.lista_autores = autoresxlibro
    libro_editar = Libro.objects.get(pk=id_libro)
    form_edicion = LibroForm(instance=libro_editar, initial=libro_editar.__dict__)
    if request.method == 'POST':
        form_edicion = LibroForm(request.POST, instance=libro_editar, initial=libro_editar.__dict__)

        if form_edicion.has_changed():
            print(id_libro)
            if form_edicion.is_valid():
                libro_nuevo = form_edicion.save(commit=False)
                libro_nuevo.titulo_libro = libro_nuevo.titulo_libro.upper()
                libro_nuevo.pais = libro_nuevo.pais.upper()
                libro_nuevo.ciudad = libro_nuevo.ciudad.upper()
                libro_nuevo.idioma = libro_nuevo.idioma.upper()
                libro_nuevo.editorial = libro_nuevo.editorial.upper()
                libro_nuevo.save()
                form_edicion.save()
                return HttpResponseRedirect("/libro/listar/")
        else:
            return HttpResponseRedirect("/libro/listar/")
        
    return render(request, 'mostrar_libro.html', {'libros':libros, 'edicion':True, 'form_edicion':form_edicion,'profile':profile})


@login_required
def activacion_libro(request, id_libro):
    lib = Libro.objects.get(pk=id_libro)
    if lib.activo:
        lib.activo = False
    else:
        lib.activo = True
    lib.save()
    return HttpResponseRedirect("/libro/listar/")




def crear_noticia(request):
    global profile
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia= form.save(commit=False)
            noticia.titulo_noticia=libro.titulo_noticia.upper()
            form.save()
            return render(request, 'crear_noticia.html', {'form': NoticiaForm(), 'exito': True,'profile':profile})
    else:
        form = NoticiaForm()
    return render(request, 'crear_noticia.html', {'form': form, 'exito': False,'profile':profile})

def crop_pic(request):

    response_data = {"status":"error", 'message':'Only Post Accepted'}
    if request.method == 'POST':

        
        form = CropForm(request.POST)
        if form.is_valid():
            # get the url of the working image i.e. www.example.com/media/pictures/uploaded_image.png
            image_url = form.cleaned_data['imgUrl'] 

            # get the root url for media files i.e. www.example.com/media/      
            media_url = default_storage.base_url 

            # strip the root url off the image url to get it's path i.e. pictures/uploaded_image.png 
            # The purpose of splitting the url at '?' is in the case a querystring is attached to the URL
            image_path = image_url

            #pic = Picture.objects.get(image=image_path)
            image_path = re.sub('^data:image/.+;base64,', '', image_url)
            
            original = Image.open(BytesIO(base64.b64decode(image_path)))
            newim = original.resize(
                        (int(form.cleaned_data['imgW']), int(form.cleaned_data['imgH'])), 
                        Image.ANTIALIAS
                        )

            x1 = int(form.cleaned_data['imgX1']) 
            y1 = int(form.cleaned_data['imgY1']) 
            x2 = int(form.cleaned_data['cropW']) + x1
            y2 = int(form.cleaned_data['cropH']) + y1

            newim = newim.crop((x1,y1,x2,y2))
            
            
            newim.save("media/"+datetime.datetime.today().strftime("%Y-%m-%d")+".png","PNG")
            

            #old_image.close()
            
            response_data = {
                "status":"success",
                "url":media_url+datetime.datetime.today().strftime("%Y-%m-%d")+".png",
                }
        else:
            response_data = {"status":"error", 'message':form.errors}

    # Croppic will parse the information returned into json. content_type needs 
    # to be set as 'text/plain'
    return HttpResponse(json.dumps(response_data), 
                        content_type="text/plain")

