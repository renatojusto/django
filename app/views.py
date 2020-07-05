from django.shortcuts import render

# Create your views here.
from app.models import Aula


def aula_list(request):
    aulas = Aula.objects.all();
    return render(
        request,
        'aula_list.html',
        {
            'aulas': aulas
        }
    )