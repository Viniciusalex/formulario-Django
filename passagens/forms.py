from email.mime import image
from secrets import choice
from django import forms
from django.forms import Textarea
from tempus_dominus.widgets  import  DatePicker
from datetime import datetime
from passagens.classes_viagem import tipos_de_classes
from passagens.validation import *

class PassagemForms(forms.Form):
    nome_sobrenome = forms.CharField(label='Nome e sobrenome', max_length=100)
    origem  = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker)
    data_volta = forms.DateField(label='Volta', widget=DatePicker)
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='classe do voo', choices = tipos_de_classes)
    informacao = forms.CharField(
        label='informções extras',
        max_length=150,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='Email', max_length=150)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}
        campo_tem_algum_numero(origem,'origem', lista_de_erros)
        campo_tem_algum_numero(destino,'destino', lista_de_erros)
        campos_nao_podem_ser_iguais(origem, destino , lista_de_erros)
        data_de_volta_nao_pode_ser_menor_que_data_ida(data_ida, data_volta, lista_de_erros)
        data_de_ida_nao_pode_ser_menor_que_data_da_pesquisa(data_ida, data_pesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data