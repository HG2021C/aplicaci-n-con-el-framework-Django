from django.shortcuts import render
from .models import Curso

def home(request):
    cursosListados = Curso.objects.all()
    return render(request, "ejemplo5app\gestionCursos.html", {"cursos":cursosListados})

    