from django.urls import URLPattern

from rest_framework import routers
from .viewset import NacViews, NomencViews, AlumnoViews, CursoViews, ModuloViews, AlumPorModViews


router = routers.SimpleRouter()
router.register  ('appcentro', NacViews)
router.register  ('appNomenc', NomencViews)
router.register  ('appAlum', AlumnoViews)
router.register  ('appCurso', CursoViews)
router.register  ('appModulo', ModuloViews)
router.register  ('appAlumPorMod', AlumPorModViews)

urlpatterns = router.urls
