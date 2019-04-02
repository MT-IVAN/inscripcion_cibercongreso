from django import forms

from apps.curso.models import Curso, Persona

class CursoFrom(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__" 


        field = [
            'nombre',
            'cupo',
            'fecha',
            'hI',
            'hF',
            'lugar',
            'ponente',
        ]
        labels = {
            'nombre': 'Nombre',
            'cupo': 'Cantidad de cupos disponibles',
            'fecha': 'Fecha y hora del curso',
            'hI': 'Hora de inicio',
            'hF': 'Hora de finalizacion',
            'lugar': 'Lugar',
            'ponente': 'Ponente',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), 
            'cupo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha' : forms.TextInput(attrs={'class': 'form-control'}),
            'hI' : forms.TextInput(attrs={'class': 'form-control'}),
            'hF' : forms.TextInput(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'ponente': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class PersonaFrom(forms.ModelForm):
    class Meta:
        model = Persona
        include = ('id',)
        fields = "__all__" 


        field = [
            'id',
        ]
        labels = {
            'id': 'Identificación',
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),            
        }