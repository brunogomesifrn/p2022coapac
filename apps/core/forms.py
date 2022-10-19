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
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['area'].empty_label = None

class FormUsuario(ModelForm):
    class Meta: 
        model:Usuario
        fields:['matricula, nome, senha, telefone, objeto']
        widgets = {
            'objeto': forms.CheckboxSelectMultiple(),
        }

class FormEmprestimo(ModelForm):
    class Meta: 
        model:Emprestimo
        fields:['quantidade, data_emprestimo, data_devolucao, observacao, objeto']
        widgets = {
            'objeto': forms.CheckboxSelectMultiple(),
        }