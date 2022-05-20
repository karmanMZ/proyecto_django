from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso


# Create your views here.


def cursos(request):
    cursos = Curso.objects.all()
    
    return HttpResponse(cursos)

def alta_curso(request, nombre):
    curso = Curso(nombre="JS", camada = 245864)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} Camada"