from django.forms import ModelForm
from .models import Tipo, Objeto, Usuario, Emprestimo

class FormTipo(ModelForm):
    class Meta: 
        model:Tipo
        fields:['nome']

class FormObjeto(ModelForm):
    class Meta: 
        model:Objeto
        fields:['nome, prazo, tipo']
        widgets = {
            'tipo': forms.RadioSelect(),
        }

class FormUsuario(ModelForm):
    class Meta: 
        model:Usuario
        fields:['matricula, nome, senha, telefone']
    

class FormEmprestimo(ModelForm):
    class Meta: 
        model:Emprestimo
        fields:['quantidade, data_emprestimo, data_devolucao, observacao, objeto, usuario']
        widgets = {
            'objeto': forms.CheckboxSelectMultiple(),
            'usuario': forms.RadioSelect()
        }