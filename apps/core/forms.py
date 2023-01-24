from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Tipo, Objeto, Usuario, Emprestimo

class FormTipo(ModelForm):
    class Meta():
        model = Tipo
        fields = ['nome_tipo']

class FormObjeto(ModelForm):
    class Meta():
        model = Objeto
        fields = ['nome_objeto', 'prazo', 'tipos']
        widgets = {
            'tipo': forms.RadioSelect(), 
        }
        
class FormUsuario(UserCreationForm):
    class Meta(): 
        model=Usuario
        fields=['matricula', 'nome', 'email', 'password1', 'password2', 'telefone']
    

class FormEmprestimo(ModelForm):
    class Meta():
        model=Emprestimo
        fields=['matricula', 'nome_servidor', 'observacao', 'objeto']
        widgets = {
            'objeto': forms.RadioSelect(), 
            }