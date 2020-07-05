from django.shortcuts import render

# Create your views here.
from app.models import Class


def class_list(request):
    classes = Class.objects.all();
    return render(
        request,
        'class_list.html',
        {
            'classes': classes
        }
    )