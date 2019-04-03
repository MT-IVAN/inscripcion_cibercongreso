from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.curso.models import Curso, Persona
from apps.curso.forms import CursoFrom, PersonaFrom
from django.views.generic import ListView, CreateView
from django.urls import reverse, reverse_lazy, resolve
import json


# Create your views here.

def mostrarIncripcion(request):
    id_curso = request.POST["curso_id"]
    curso = Curso.objects.get(id=id_curso)
    return render(request, 'cursos/curso_form.html', {'form':curso})

def comprobarInscripcion(request):
    id_curso = request.POST["curso_id"]
    cupoCurso = Curso.objects.get(id=id_curso)
    if cupoCurso.cupo >0:
        #Obtengo la cedula que es ingresada
        cedula = request.POST['cedula']
        persona = Persona()
        try:
            #verifico que la persona exista
            persona = Persona.objects.get(id=cedula)
        except persona.DoesNotExist:
            #si no existe la persona
            persona = "La cedula '"+ cedula + "' no se encuentra registrada. Si ya realizo el pago de la incripciòn del cibercongreso por favor espere 24 horas para que se pueda inscribir en uno de los talleres disponibles"
            return render(request, 'cursos/cedula_no_encontrada.html', {'form':persona})
            #incribo a la persona si no esta registrada en nada
        if persona.curso =='' or persona.curso is None:
            persona.curso_id = int(id_curso)
            curso = Curso.objects.get(id=id_curso)
            curso.cupo = curso.cupo -1
            curso.save()
            persona.save()
            return render(request, 'cursos/registro_exitoso.html', {'form':persona})
            #valido cuando se registra en el mismo curso
        elif persona.curso_id is not None and persona.curso_id == id_curso:
            persona = 'Ya estás registrado en este taller'
            return render(request, 'cursos/registro_mismo_curso.html', {'form':persona})
            #cuando la persona se intenta registrar en un curso diferente al que esta registrado
        elif persona.curso_id is not None and persona.curso_id != id_curso:
            #tengo que sacar el registro de la persona del curos donde esta registrada
            cursoAntiguo = Curso.objects.get(id = persona.curso_id)
            cursoNuevo = Curso.objects.get(id = id_curso)
            registroNuevo = 'Actualmente te encuentras registrado en el curso de "'+cursoAntiguo.nombre+'". Puedes incribirte en el curso de "'+cursoNuevo.nombre+'" haciendo click en el boton aceptar. Recuerda que solo puedes estar registrado en un solo curso.'
            return render(request, 'cursos/cambio_de_curso.html', {'form':registroNuevo, 'formDos':persona, 'cursoAntiguo':cursoAntiguo, 'cursoNuevo':cursoNuevo })
    else:
        return render(request, 'cursos/cupo_completo.html')

def cambiarIncripcionCurso(request):
    id_curso_nuevo = request.POST['cursoNuevo']
    cursoNuevo = Curso.objects.get(id = id_curso_nuevo)
    if(cursoNuevo.cupo >0):
        id_curso_viejo = request.POST['cursoAntiguo'] 
        id_persona = request.POST['persona']
        cursoViejo = Curso.objects.get(id = id_curso_viejo)
        #print(id_persona)
        persona = Persona.objects.get(id= id_persona)
        cursoViejo.cupo = cursoViejo.cupo + 1   
        cursoViejo.save()
        persona.curso_id = cursoNuevo.id
        persona.save()
        cursoNuevo.cupo = cursoNuevo.cupo - 1
        cursoNuevo.save()
        return render(request, 'cursos/registro_exitoso.html')
    else:
        return render(request, 'cursos/cupo_completo.html')
    




class ListarCursos(ListView):
    model = Curso
    template_name = 'cursos/curso_list.html'


class CreateForm(CreateView):
    model = Persona
    fields = ['id']
    template_name = 'curso_form.html'
    success_url = reverse_lazy('incripcion')

# class PersonaApi(viewsets.ModelViewSet):
#     queryset =  Persona.objects.all()
#     serializer_class = UserSerializer
