from django.urls import path

from app.views import class_list

urlpatterns = [
    path('class_list/', class_list),
]