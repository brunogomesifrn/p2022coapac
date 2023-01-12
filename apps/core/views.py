from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Tipo, Objeto, Usuario, Emprestimo
from .forms import FormTipo, FormObjeto, FormUsuario, FormEmprestimo

#Crud de obejtos
def objeto_listar(request):
    objeto = Objeto.objects.all()
    contexto ={
        'listar_objetos': objeto
    }
    return render(request, 'objetos/objetos_lista.html', contexto)

def objeto_cadastrar(request):
    form = FormObjeto(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('objeto_listar')
    contexto = {
        'form' : form
    }
    return render(request, 'objetos/objetos_cad.html', contexto)

def objeto_editar(request, id):
    objeto = Objeto.objects.get(pk=id)

    form = FormObjeto(request.POST or None, instance=objeto)

    if form.is_valid():
        form.save()
        return redirect('objeto_listar')

    contexto = {
        'form' : form
    }
    return render(request, 'objetos/objetos_cad.html', contexto)

def obejto_remover(request,id):
    objeto = Objeto.objects.get(pk=id)
    objeto.delete()
    return redirect('objeto_listar')

#Crud de tipos de objetos
def tipo_listar(request):
    tipo = Tipo.objects.all()
    contexto ={
        'listar_tipo': tipo
    }
    return render(request, 'tipo_objetos/tipo_lista.html', contexto)

def tipo_cadastrar(request):
    form = FormTipo(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('tipo_listar')
    contexto = {
        'form' : form
    }
    return render(request, 'tipo_objetos/tipo_cad.html', contexto)

def tipo_editar(request,id):
    tipo = Tipo.objects.get(pk=id)

    form = FormTipo(request.POST or None, instance=tipo)

    if form.is_valid():
        form.save()
        return redirect('tipo_listar')

    contexto = {
        'form' : form 
    }
    return render(request, 'tipo_objetos/tipo_cad.html', contexto)

def tipo_remover(request,id):
    tipo = Tipo.objects.get(pk=id)
    tipo.delete()
    return redirect('tipo_listar')


#Crud de emprestimos
def emprestimo_listar(request):
    emprestimo = Tipo.objects.all()
    contexto ={
        'listar_emprestimo': emprestimo
    }
    return render(request, 'emprestimos/listar.html')

def emprestimo_cadastro(request):
    form = FormEmprestimo(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('emprestimo')
    contexto = {
        'form' : form
    }
    return render(request, 'emprestimos/novo.html',contexto)

def emprestimo_editar(request,id):
    emprestimo = Emprestimo.objects.get(pk=id)

    form = FormEmprestimo(request.POST or None, instance=tipo)

    if form.is_valid():
        form.save()
        return redirect('emprestimo')

    contexto = {
        'form' : form 
    }
    return render(request, 'emprestimos/novo.html', contexto)

def emprestimo_remover(request,id):
    emprestimo = Emprestimo.objects.get(pk=id)
    emprestimo.delete()
    return redirect('emprestimo')

def emprestimo(request):
    return render(request, 'emprestimos/emprestimo.html')

#crud de usuarios
def usuario_listar(request):
    usuario = Usuario.objects.all()
    contexto ={
        'listar_usuarios': usuario
    }
    return render(request, 'usuario/usuario_listar.html')

def usuario_remover(request,id):
    usuario = Usuario().objects.get(pk=id)
    usuario.delete()
    return redirect('usuario_listar')



def perfil(request):
    return render(request, 'index.html')

def devolucao(request):
    return render(request, 'devolucao.html')

#Autenticação
def autenticacao(request):
    if request.POST:
        matricula = request.POST['matricula']
        password = request.POST['senha']
        user = authenticate(request, username=matricula, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'registration\login.html')
    else:
        return render(request, 'registration\login.html')

def desconectar(request):
    logout(request)
    return redirect('login')

def registro(request):
    form = FormUsuario(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form': form
    }
    return render(request, 'registration/registro.html', contexto)