from rest_framework import viewsets
from .serializer import NacSerializer, NomencSerializer, AlumnoSerializer, CursoSerializer, ModuloSerializer, AlumPorModSerializer
from .models import Nacionalidad, Nomenclador, Alumnos, Cursos, Modulos, AlumnosPorModulos

class NacViews(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacSerializer

class NomencViews(viewsets.ModelViewSet):
    queryset = Nomenclador.objects.all()
    serializer_class = NomencSerializer

class AlumnoViews(viewsets.ModelViewSet):
    queryset = Alumnos.objects.all()
    serializer_class = AlumnoSerializer

class CursoViews(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializer

class ModuloViews(viewsets.ModelViewSet):
    queryset = Modulos.objects.all()
    serializer_class = ModuloSerializer

class AlumPorModViews(viewsets.ModelViewSet):
    queryset = AlumnosPorModulos.objects.all()
    serializer_class = AlumPorModSerializer