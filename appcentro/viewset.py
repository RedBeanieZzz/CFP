from rest_framework import viewsets
from .serializer import AlumnoSerializer, CursoSerializer, NacionalidadSerializer, NomencladorSerializer, ModulosSerializer, AlumModuloSerial
from .models import Alumnos, Cursos, Nomenclador, Modulos, AlumnosPorModulos, Nacionalidad

class AlumnoViewSet (viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class = AlumnoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializer

class NacionViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer

class NomenViewSet(viewsets.ModelViewSet):
    queryset = Nomenclador.objects.all()
    serializer_class = NomencladorSerializer

class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulos.objects.all()
    serializer_class = ModulosSerializer

class AlumPorModViewSet(viewsets.ModelViewSet):
    queryset = AlumnosPorModulos.objects.all()
    serializer_class = AlumModuloSerial