from multiprocessing import context
from django import forms
from django.shortcuts import render
from django.urls import is_valid_path
from passagens.forms import PassagemForms

def index(request):
    form = PassagemForms()
    contexto = {'form': form} 
    return render(request, 'index.html', contexto)

def revisao_passagem(request):
    if request.method =='POST':
        form = PassagemForms(request.POST)
        if form.is_valid():
            contexto = {'form': form} 
            return render(request, 'revisao_passagem.html', contexto)
        else:
            contexto = {'form': form} 
            return render(request, 'index.html', contexto)