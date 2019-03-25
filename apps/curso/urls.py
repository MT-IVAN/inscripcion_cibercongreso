from django.urls import path, include
from apps.curso.views import CreateForm, ListarCursos, mostrarIncripcion, comprobarInscripcion, cambiarIncripcionCurso

urlpatterns = [
    path('', ListarCursos.as_view(), name='curso_listar'),
    path('inscripcion/<int:id_curso>', mostrarIncripcion, name='incripcion'),
    path('comprobar/<int:id_curso>', comprobarInscripcion, name='comprobar'),
    path('cambiar_curso', cambiarIncripcionCurso, name='cambiar'),
     
]
