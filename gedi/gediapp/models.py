# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    foto = models.ImageField(upload_to='fotos_usuarios', blank=True)


class Integrante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    horas_dedicacion = models.IntegerField(default=0)
    fecha_inicio_vin = models.DateField()
    fecha_fin_vin = models.DateField(null=True,blank=True)
    activo = models.BooleanField(default=True)
    actual = models.BooleanField(default=True)

    def __str__(self):
        return self.nombres + " " + self.apellidos


class Articulo(models.Model):
    autores = models.ManyToManyField(Integrante)
    COMPLETO = 'COM'
    CORTO = 'COR'
    REVISION = 'RE'
    CASOCLINICO = 'CC'
    TIPO_ARTICULO_CHOICES = (
        (COMPLETO, 'Completo'),
        (CORTO, 'Corto'),
        (REVISION, 'Revisión'),
        (CASOCLINICO, 'Caso clínico'),
    )
    tipo_articulo = models.CharField(
        max_length=100, choices=TIPO_ARTICULO_CHOICES, default=COMPLETO)
    titulo_articulo = models.TextField()
    pagina_inicial = models.IntegerField()
    pagina_final = models.IntegerField()
    idioma = models.CharField(max_length=100)
    anio = models.IntegerField()
    ENERO = 1
    FEBRERO = 2
    MARZO = 3
    ABRIL = 4
    MAYO = 5
    JUNIO = 6
    JULIO = 7
    AGOSTO = 8
    SEPTIEMBRE = 9
    OCTUBRE = 10
    NOVIEMBRE = 11
    DICIEMBRE = 12
    MES_CHOICES = (
        (ENERO, 'Enero'),
        (FEBRERO, 'Febrero'),
        (MARZO, 'Marzo'),
        (ABRIL, 'Abril'),
        (MAYO, 'Mayo'),
        (JUNIO, 'Junio'),
        (JULIO, 'Julio'),
        (AGOSTO, 'Agosto'),
        (SEPTIEMBRE, 'Septiembre'),
        (OCTUBRE, 'Octubre'),
        (NOVIEMBRE, 'Noviembre'),
        (DICIEMBRE, 'Diciembre'),
    )
    mes = models.IntegerField(
         choices=MES_CHOICES, default=ENERO)
    revista = models.CharField(max_length=100)
    volumen = models.IntegerField()
    fasciculo = models.CharField(max_length=20)
    serie_revista = models.CharField(max_length=30)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    PAPEL = 'P'
    ELECTRONICO = 'E'
    DIVULGACION_CHOICES = (
        (PAPEL, 'Papel'),
        (ELECTRONICO, 'Electrónico'),
    )
    medio_divulgacion = models.CharField(
        max_length=100, choices=DIVULGACION_CHOICES, default=PAPEL)
    sitio_web = models.URLField(max_length=100) #Correccion para que funcione bien
    DOI = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo_articulo


class Softwares(models.Model):
    COMPUTACIONAl = 'Computacional'
    MULTIMEDIA = 'Multimedia'
    OTRO = 'Otro'
    TIPO_SOFTWARE_CHOICES = (
        (COMPUTACIONAl, 'Computacional'),
        (MULTIMEDIA, 'Multimedia'),
        (OTRO, 'Otro'),
    )
    tipo = models.CharField(
        max_length=100, choices=TIPO_SOFTWARE_CHOICES, default=COMPUTACIONAl)
    nombre = models.CharField(max_length=250)
    pais = models.CharField(max_length=100)
    year = models.IntegerField(default=0)

    RESTRINGIDO = 'Restringido'
    NORESTRINGIDO = 'No Restringido'
    DISPONIBILIDAD_SOFTWARE = (
        (RESTRINGIDO, 'Restringido'),
        (NORESTRINGIDO, 'No Restringido'),
    )

    disponibilidad = models.CharField(
        max_length=100, choices=DISPONIBILIDAD_SOFTWARE, default=RESTRINGIDO)
    web = models.URLField(max_length=100)
    nombre_comercial = models.CharField(max_length=100)
    nombre_proyecto = models.CharField(max_length=250)
    institucion_financiadora = models.CharField(max_length=100)
    autores = models.ManyToManyField(Integrante)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class TrabajosDirigidos(models.Model):

    autores = models.ManyToManyField(Integrante)

    TMAESTRIA_TESPECIALIDADMEDICA = 'Trabajo de grado de maestria o especialidad medica'
    TESISDOCTORADO = 'Tesis de doctorado'
    MONOGRAFIA = 'Monografia de conclusion de curso de perfeccionamiento / especializacion'
    CONCLUSIONPREGRADO = 'Trabajo de conclusion de curso de pregrado'
    INICIACIONCIENTIFICA = 'Iniciacion cientifica'
    TUTORIA = 'Trabajos dirigidos / Tutorias de otro tipo'
    TIPO_TRABAJO_DIRIGIDO = (
        (TMAESTRIA_TESPECIALIDADMEDICA,
         'Trabajo de grado de maestria o especialidad medica'),
        (TESISDOCTORADO, 'Tesis de doctorado'),
        (MONOGRAFIA,
         'Monografia de conclusion de curso de perfeccionamiento / especializacion'),
        (CONCLUSIONPREGRADO, 'Trabajo de conclusion de curso de pregrado'),
        (INICIACIONCIENTIFICA, 'Iniciacion cientifica'),
        (TUTORIA, 'Trabajos dirigidos / Tutorias de otro tipo'),
    )
    tipo = models.CharField(
        max_length=100, choices=TIPO_TRABAJO_DIRIGIDO, default=CONCLUSIONPREGRADO)
    nombre = models.CharField(max_length=250)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    TUTOR = 'Tutor principal'
    COTUTOR = 'Cotutor/asesor'
    ASESOR = 'Asesor de orientacion'
    TIPO_ORIENTACION_TDIRIGIDO = (
        (TUTOR, 'Tutor principal'),
        (COTUTOR, ' Cotutor/asesor'),
        (ASESOR, 'Asesor de orientacion'),
    )
    tipo_orientacion = models.CharField(
        max_length=100, choices=TIPO_ORIENTACION_TDIRIGIDO, default=TUTOR)
    nombre_estudiante = models.CharField(max_length=100)
    programa_academico = models.CharField(max_length=100)
    numero_paginas = models.IntegerField(default=0)

    APROBADA = 'Aprobada'
    MERITORIA = 'Distincion meritoria'
    LAUREADA = 'Distincion laureada'
    VALORACION_SOFTWARE = (
        (APROBADA, 'Aprobada'),
        (MERITORIA, 'Distincion meritoria'),
        (LAUREADA, 'Distincion laureada'),
    )
    valoracion = models.CharField(
        max_length=100, choices=VALORACION_SOFTWARE, default=APROBADA)
    institucion = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre


class CapitulosLibros(models.Model):
    autores = models.ManyToManyField(Integrante)
    titulo_capitulo_libro=models.CharField(max_length=200)
    titulo_libro=models.CharField(max_length=200)
    ISBN_libro=models.CharField(max_length=100)
    anio_presentacion = models.IntegerField()
    ENERO = 1
    FEBRERO = 2
    MARZO = 3
    ABRIL = 4
    MAYO = 5
    JUNIO = 6
    JULIO = 7
    AGOSTO = 8
    SEPTIEMBRE = 9
    OCTUBRE = 10
    NOVIEMBRE = 11
    DICIEMBRE = 12
    MES_CHOICES = (
        (ENERO, 'Enero'),
        (FEBRERO, 'Febrero'),
        (MARZO, 'Marzo'),
        (ABRIL, 'Abril'),
        (MAYO, 'Mayo'),
        (JUNIO, 'Junio'),
        (JULIO, 'Julio'),
        (AGOSTO, 'Agosto'),
        (SEPTIEMBRE, 'Septiembre'),
        (OCTUBRE, 'Octubre'),
        (NOVIEMBRE, 'Noviembre'),
        (DICIEMBRE, 'Diciembre'),
    )
    mes_presentacion=models.IntegerField(choices=MES_CHOICES, default=ENERO)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo_capitulo_libro

class Libro(models.Model):
    autores = models.ManyToManyField(Integrante)
    titulo_libro = models.TextField()
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    anio = models.IntegerField()
    idioma = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)
    volumen = models.IntegerField()
    paginas = models.IntegerField()
    editorial = models.CharField(max_length=100)

    ENERO = 1
    FEBRERO = 2
    MARZO = 3
    ABRIL = 4
    MAYO = 5
    JUNIO = 6
    JULIO = 7
    AGOSTO = 8
    SEPTIEMBRE = 9
    OCTUBRE = 10
    NOVIEMBRE = 11
    DICIEMBRE = 12
    MES_CHOICES = (
        (ENERO, 'Enero'),
        (FEBRERO, 'Febrero'),
        (MARZO, 'Marzo'),
        (ABRIL, 'Abril'),
        (MAYO, 'Mayo'),
        (JUNIO, 'Junio'),
        (JULIO, 'Julio'),
        (AGOSTO, 'Agosto'),
        (SEPTIEMBRE, 'Septiembre'),
        (OCTUBRE, 'Octubre'),
        (NOVIEMBRE, 'Noviembre'),
        (DICIEMBRE, 'Diciembre'),
    )
    mes = models.IntegerField(
         choices=MES_CHOICES, default=ENERO)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo_libro

class Noticias(models.Model):
    titulo_noticia = models.TextField()
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    pic = models.ImageField(upload_to="news/")

    def __str__(self):
        return self.titulo_noticia