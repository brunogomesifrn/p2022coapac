from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Tipo, Objeto, Usuario, Emprestimo
from .forms import FormTipo, FormObjeto, FormUsuario, FormEmprestimo
from datetime import date

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
        return redirect('usuario_listar')
    contexto = {
        'form': form
    }
    return render(request, 'registration/registro.html', contexto)


#Crud de obejtos
@login_required
def objeto_listar(request):
    nome_digitado = ''
    objeto = []
    if request.POST:
        if request.POST['nome_objeto']=='':
            objeto = Objeto.objects.all().order_by('nome_objeto')
        else:
            nome_digitado = request.POST['nome_objeto']
            objeto = Objeto.objects.filter(nome_objeto__contains=nome_digitado).order_by('nome_objeto')
    else:
        objeto = Objeto.objects.all().order_by('nome_objeto')
    contexto ={
        'listar_objetos': objeto,
        'nome_digitado': nome_digitado
    }
    return render(request, 'objetos/objetos_lista.html', contexto)




'''
emprestimos = []
    matricula_digitada=""
    if request.POST:
        if request.POST['usuario']=='':
            emprestimos = Emprestimo.objects.all()
        else:
            matricula_digitada = request.POST['usuario']
            emprestimos = Emprestimo.objects.filter(matricula = matricula_digitada).filter(data_devolucao = None).order_by('data_emprestimo')
    else:
        emprestimos = Emprestimo.objects.all().order_by('data_emprestimo')
    contexto ={
        'listar_emprestimo': emprestimos,
        'matricula_digitada': matricula_digitada
    }
    return render(request, 'emprestimos/devolucao.html', contexto)

'''

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
    tipo = []
    nome_digitada=""
    if request.POST:
        if request.POST['nome_tipo']=='':
            tipo = Tipo.objects.all()
        else:
            nome_digitada = request.POST['nome_tipo']
            tipo = Tipo.objects.filter(nome_tipo=nome_digitada).order_by('nome_tipo')
    else:
        tipo = Tipo.objects.all()
    contexto ={
        'listar_tipo': tipo,
        'nome_digitada': nome_digitada
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
    emprestimos = []
    matricula_digitada=""
    if request.POST:
        if request.POST['usuario']=='':
            emprestimos = Emprestimo.objects.all()
        else:
            matricula_digitada = request.POST['usuario']
            emprestimos = Emprestimo.objects.filter(matricula = matricula_digitada.strip()).order_by('data_emprestimo')
    else:
        emprestimos = Emprestimo.objects.all().order_by('-data_emprestimo')
    contexto ={
        'listar_emprestimo': emprestimos,
        'matricula_digitada': matricula_digitada
    }

    # VERIFICAR STATUS

    return render(request, 'emprestimos/listar.html', contexto)
    

@login_required
def emprestimo_cadastro(request):
    form = FormEmprestimo(request.POST or None)

    if form.is_valid(): 
        emprestimo = form.save(commit=False)
        emprestimo.responsavel = request.user
        emprestimo.data_emprestimo = date.today()
        emprestimo.save()
        return redirect('emprestimo')
    contexto = {
        'form' : form
    }
    return render(request, 'emprestimos/novo.html',contexto)

@login_required
def emprestimo_editar(request,id):
    emprestimo = Emprestimo.objects.get(pk=id)

    form = FormEmprestimo(request.POST or None, instance=emprestimo)

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
    emprestimo = Emprestimo.objects.all()
    contexto ={
        'listar_emprestimo': emprestimo
    }
    return render(request, 'emprestimos/emprestimo.html', contexto)

@login_required
#crud de usuarios
def usuario_listar(request):
    usuario = []
    nome_digitada=""
    if request.POST:
        if request.POST['nome']=='':
            usuario = Usuario.objects.all()
        else:
            nome_digitada = request.POST['nome']
            usuario = Usuario.objects.filter(nome=nome_digitada.strip()).order_by('matricula')
    else:
        usuario = Usuario.objects.all().order_by('matricula')
    contexto ={
        'listar_usuario': usuario,
        'nome_digitada': nome_digitada
    }
    return render(request, 'usuario/usuario_listar.html', contexto)

@login_required
def usuario_editar(request,id):
    usuario = Usuario.objects.get(pk=id)

    form = FormUsuario(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('usuario_listar')

    contexto = {
        'form' : form 
    }
    return render(request, 'registration/registro.html', contexto)

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
def listar_devolução(request):
    emprestimos = []
    matricula_digitada=""
    if request.POST:
        if request.POST['usuario']=='':
            emprestimos = Emprestimo.objects.all()
        else:
            matricula_digitada = request.POST['usuario']
            emprestimos = Emprestimo.objects.filter(matricula__contains = matricula_digitada.strip()).filter(data_devolucao = None).order_by('data_emprestimo')
    else:
        emprestimos = Emprestimo.objects.all().order_by('data_emprestimo')
    contexto ={
        'listar_emprestimo': emprestimos,
        'matricula_digitada': matricula_digitada
    }
    return render(request, 'emprestimos/devolucao.html', contexto)

@login_required
def devolucao(request):
    emprestimos = []
    if request.POST:
        matricula_digitada = request.POST['usuario']
        emprestimos = Emprestimo.objects.filter(matricula = matricula_digitada.strip()).filter(devolucao = None)
    contexto = {
        'emprestimos': emprestimos
    }
    return render(request, 'emprestimos/devolucao.html', contexto)

#Devolve o empréstimo
@login_required
def devolver(request, codigo):
        emprestimo = Emprestimo.objects.get(pk=codigo)
        emprestimo.data_devolucao = date.today()
        emprestimo.save()
        return redirect('emprestimo')

#Listagem para servidores 
def servidor(request):
    emprestimos = []
    matricula_digitada=""
    if request.POST:
        if request.POST['usuario']=='':
            emprestimos = Emprestimo.objects.all()
        else:
            matricula_digitada = request.POST['usuario']
            emprestimos = Emprestimo.objects.filter(matricula = matricula_digitada).order_by('data_emprestimo')
    else:
        emprestimos = Emprestimo.objects.all().order_by('data_emprestimo')
    contexto ={
        'listar_emprestimo': emprestimos,
        'matricula_digitada': matricula_digitada
    }
    return render(request, 'servidor.html', contexto)

def cadastro_manual(request):
    user = Usuario.objects.create_user(
        username='admin',
        email='admin@email.com',
        matricula='123456789',
        nome='Administrador',
        password='admin12345',
        telefone=000000,
        is_superuser=True)
    user.save()
    return redirect('perfil')