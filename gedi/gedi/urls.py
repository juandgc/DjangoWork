# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from gediapp.views import *
from django.contrib import admin
from django.conf import settings


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'gedi.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', inicio),
                       url(r'subir-foto/$', subir_foto),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^integrante/crear/$', crear_integrante),
                       url(r'^integrante/listar/$', mostrar_integrante),
                       url(r'^integrante/editar/(\d+)/$', editar_integrante),
                       url(r'^integrante/des-activacion/(\d+)/$', activacion_integrante),
                       url(r'^articulo/crear/$', crear_articulo),
                       url(r'^articulo/editar/(\d+)/$', editar_articulo),
                       url(r'^articulo/des-activacion/(\d+)/$', activacion_articulo),
                       url(r'^articulo/listar/$', mostrar_articulo),
                       url(r'^software/crear/$', crear_software),
                       url(r'^software/listar/', mostrar_software),
                       url(r'^software/des-activar/(\d+)/$',activacion_software),
                       url(r'^software/editar/(\d+)/$',editar_software),
                       url(r'^trabajo_dirigido/crear/$', crear_tdirigido),
                       url(r'^trabajo_dirigido/listar/$', mostrar_tdirigido),
                       url(r'^libro/crear/$',crear_libro),
                       url(r'^libro/listar/$',mostrar_libro),
                       url(r'^libro/editar/(\d+)/$', editar_libro),
                       url(r'^libro/des-activacion/(\d+)/$', activacion_libro),
                       url(r'^trabajo_dirigido/des-activar/(\d+)/$',activacion_tdirigido),
                       url(r'^trabajo_dirigido/editar/(\d+)/$',editar_tdirigido),
                       url(r'^capitulo_libro/crear/$',crear_caplibro),
                       url(r'^capitulo_libro/listar/$',mostrar_caplibro),
                       url(r'^capitulo_libro/editar/(\d+)/$',editar_caplibro),
                       url(r'^capitulo_libro/des-activacion/(\d+)/$',activacion_caplibro),
                       url(r'^noticia/crear/$',crear_noticia),
                       url(r'^noticia/crear/crop_pic/$', crop_pic, name='crop_pic'),
                       url(r'^login/$', iniciar_sesion),
                       url(r'^logout/$', cerrar_sesion),
                       url(r'^media/(?P<path>.*)$','django.views.static.serve',
                               {'document_root':settings.MEDIA_ROOT,} ),
)
