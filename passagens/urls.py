from unicodedata import name
from django.urls import path
from . import views


urlpatterns= [
    path('', views.index, name='index'),
    path('revisao_passagem', views.revisao_passagem, name='revisao_passagem')
]