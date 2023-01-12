from django.forms import ModelForm
from django import forms
from .models import Tipo, Objeto, Usuario, Emprestimo

class FormTipo(ModelForm):
    class Meta():
        model = Tipo
        fields = ['nome']

class FormObjeto(ModelForm):
    class Meta():
        model = Objeto
        fields = ['nome', 'prazo', 'tipos']
        widgets = {
            'tipo': forms.RadioSelect(), 
        }
        

class FormUsuario(ModelForm):
    class Meta(): 
        model=Usuario
        fields=['matricula', 'nome', 'email', 'senha', 'telefone']
    

class FormEmprestimo(ModelForm):
    class Meta():
        model=Emprestimo
        fields=['quantidade', 'data_emprestimo', 'data_devolucao', 'observacao', 'objeto', 'usuario']
        widgets = {
            'usuario': forms.RadioSelect(),
            'objeto': forms.CheckboxSelectMultiple(),
            }