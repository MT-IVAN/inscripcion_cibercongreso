from django.urls import path, include
from apps.curso.views import CreateForm, ListarCursos, mostrarIncripcion, comprobarInscripcion, cambiarIncripcionCurso, PersonaApi
from rest_framework import routers



router = routers.DefaultRouter()
router.register('users', PersonaApi)


urlpatterns = [
    path('', ListarCursos.as_view(), name='curso_listar'),
    path('inscripcion/<int:id_curso>', mostrarIncripcion, name='incripcion'),
    path('comprobar/<int:id_curso>', comprobarInscripcion, name='comprobar'),
    path('cambiar_curso', cambiarIncripcionCurso, name='cambiar'),
    path('api',include(router.urls)),
     
]
