from django.urls import path

from app.views import aula_list

urlpatterns = [
    path('aula_list/', aula_list),
    path('maratona/', aula_list),
]