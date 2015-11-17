__author__ = 'daniel'
from .models import Integrante,Articulo,Softwares,TrabajosDirigidos
from django.db.models import Max
class Dashboard():

    def totales(self):
        integrantes = Integrante.objects.all().count
        articulos = Articulo.objects.all().count
        productos_sf = Softwares.objects.all().count
        return integrantes,articulos,productos_sf

    def top_integrante(self):
        intregrantes = Integrante.objects.all()
        max = 0
        int_max = Integrante()
        art_max = 0
        soft_max = 0
        t_dir_max = 0
        for intg in intregrantes:
            art = Articulo.objects.filter(autores = intg).count()
            soft = Softwares.objects.filter(autores = intg).count()
            t_dir = TrabajosDirigidos.objects.filter(autores=intg).count()
            total = art+soft+t_dir
            if total > max :
                max = total
                int_max = intg
                art_max=art
                soft_max=soft
                t_dir_max=t_dir
        return int_max,art_max,soft_max,t_dir_max

    def software_list(self):
        datos = Softwares.objects.all()
        if len(datos) == 0:
            return ['No hay datos','No hay datos']
        elif len(datos) == 1:
            [datos[0],'No hay datos']
        year = Softwares.objects.aggregate(Max('year'))['year__max']
        softwares = Softwares.objects.filter(year= year,activo=True)
        while len(softwares) < 2:
            softwares.append(Softwares.objects.filter(year= year-1,activo=True))
        return softwares

    def trabajos_dir_list(self):
        datos  = TrabajosDirigidos.objects.all()
        if len(datos) == 0:
            return ['No hay datos','No hay datos']
        elif len(datos) == 1:
            return [datos[0],'No hay datos']
        year = TrabajosDirigidos.objects.aggregate(Max('fecha_fin'))['fecha_fin__max'].year
        trabajos = TrabajosDirigidos.objects.filter(fecha_fin__year = year,activo=True)
        while len(trabajos) < 2:
            trabajos.append(TrabajosDirigidos.objects.filter(fecha_fin__year = year-1,activo=True))
        return trabajos

    def trabajos_dir_total(self):
        return TrabajosDirigidos.objects.all().count()
