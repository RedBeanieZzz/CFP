from django.urls import URLPattern

from rest_framework import routers
from .viewset import AlumnoViewSet, CursosViewSet, NacionViewSet, NomenViewSet, ModuloViewSet, AlumPorModViewSet

router = routers.SimpleRouter()

router.register  ('appcentro', AlumnoViewSet)

router.register  ('Cursos', CursosViewSet)

router.register ('Nacionalidad', NacionViewSet)

router.register  ('Nomencladors', NomenViewSet)

router.register  ('Modulos', ModuloViewSet)

router.register  ('AlumPorMod', AlumPorModViewSet)



urlpatterns = router.urls
