from email.mime import image
from secrets import choice
from django import forms
from django.forms import Textarea
from tempus_dominus.widgets  import  DatePicker
from datetime import datetime
from passagens.classes_viagem import tipos_de_classes

class PassagemForms(forms.Form):
    origem  = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker)
    data_volta = forms.DateField(label='Volta', widget=DatePicker)
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='classe do voo', choices = tipos_de_classes)
    informacao = forms.CharField(
        label='informções extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='Email', max_length=150)