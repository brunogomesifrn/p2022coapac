from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Tipo, Objeto, Usuario, Emprestimo
from .forms import FormTipo, FormObjeto, FormUsuario, FormEmprestimo

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
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')

def desconectar(request):
    logout(request)
    return redirect('login')

@login_required
def registro(request):
    form = FormUsuario(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form': form
    }
    return render(request, 'registration/registro.html', contexto)


#Crud de obejtos
@login_required
def objeto_listar(request):
    objeto = Objeto.objects.all()
    contexto ={
        'listar_objetos': objeto
    }
    return render(request, 'objetos/objetos_lista.html', contexto)

@login_required
def objeto_cadastrar(request):
    form = FormObjeto(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('objeto_listar')
    contexto = {
        'form' : form
    }
    return render(request, 'objetos/objetos_cad.html', contexto)

@login_required
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

@login_required
def obejto_remover(request,id):
    objeto = Objeto.objects.get(pk=id)
    objeto.delete()
    return redirect('objeto_listar')

@login_required
#Crud de tipos de objetos
def tipo_listar(request):
    tipo = Tipo.objects.all()
    contexto ={
        'listar_tipo': tipo
    }
    return render(request, 'tipo_objetos/tipo_lista.html', contexto)

@login_required
def tipo_cadastrar(request):
    form = FormTipo(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('tipo_listar')
    contexto = {
        'form' : form
    }
    return render(request, 'tipo_objetos/tipo_cad.html', contexto)

@login_required
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

@login_required
def tipo_remover(request,id):
    tipo = Tipo.objects.get(pk=id)
    tipo.delete()
    return redirect('tipo_listar')

@login_required
#Crud de emprestimos
def emprestimo_listar(request):
    emprestimo = Tipo.objects.all()
    contexto ={
        'listar_emprestimo': emprestimo
    }
    return render(request, 'emprestimos/listar.html')

@login_required
def emprestimo_cadastro(request):
    form = FormEmprestimo(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('emprestimo')
    contexto = {
        'form' : form
    }
    return render(request, 'emprestimos/novo.html',contexto)

@login_required
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

@login_required
def emprestimo_remover(request,id):
    emprestimo = Emprestimo.objects.get(pk=id)
    emprestimo.delete()
    return redirect('emprestimo')

@login_required
def emprestimo(request):
    return render(request, 'emprestimos/emprestimo.html')

@login_required
#crud de usuarios
def usuario_listar(request):
    usuario = Usuario.objects.all()
    contexto ={
        'listar_usuarios': usuario
    }
    return render(request, 'usuario/usuario_listar.html')

@login_required
def usuario_remover(request,id):
    usuario = Usuario().objects.get(pk=id)
    usuario.delete()
    return redirect('usuario_listar')

@login_required
def perfil(request):
    return render(request, 'index.html')


#Lista os empréstimos sem devolução do usuário
@login_required
def devolucao(request):
    emprestimos = []
    if request.POST:
        matricula_digitada = request.POST['usuario']
        emprestimos = Emprestimo.objects.filter(matricula = matricula_digitada).filter(devolucao = None)
    contexto = {
        'emprestimos': emprestimos
    }
    return render(request, 'emprestimos/devolucao.html', contexto)

#Devolve o empréstimo
def devolver(request, codigo):
        emprestimo = Emprestimo.objects.get(pk=codigo)
        emprestimo.data_devolucao = datetime.date.today()
        emprestimo.save()
        return redirect('emprestimo')

