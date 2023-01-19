"""coapac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from apps.core.views import emprestimo, devolucao, devolver, emprestimo_listar,emprestimo_remover, emprestimo_cadastro, emprestimo_editar, perfil, autenticacao, desconectar, registro, usuario_listar,usuario_remover
from apps.core.views import objeto_cadastrar, obejto_remover,objeto_editar, objeto_listar, tipo_cadastrar,tipo_editar,tipo_listar, tipo_remover, emprestimo_editar,emprestimo_remover, usuario_editar, listar_devolução

urlpatterns = [
    #Objetos
    path('objetos/', objeto_listar, name='objeto_listar'),
    path('cadastrar_objetos/', objeto_cadastrar, name='objetos_cadastrar'),
    path('editar_objetos/<int:id>/', objeto_editar, name='objeto_editar'),
    path('deletar_objetos/<int:id>/', obejto_remover, name='obejto_remover'),

    #Tipo
    path('tipos/', tipo_listar, name='tipo_listar'),
    path('cadastrar_tipos/', tipo_cadastrar, name='tipo_cadastrar'),
    path('atualizar_tipos/<int:id>/', tipo_editar, name='tipo_editar'),
    path('deletar_tipos/<int:id>/', tipo_remover, name='tipo_remover'),

    #Emprestimos
    path('emprestimo/',emprestimo, name="emprestimo"),
    path('devolver/<str:codigo>/',devolver, name="devolver"),
    path('devolução/', listar_devolução, name='listar_devolucao'),
    path('listar/', emprestimo_listar, name="emprestimo_listar"),
    path('novo/',emprestimo_cadastro, name="emprestimo_cadastro"),
    path('atualizar_emprestimo/<int:id>/', emprestimo_editar, name='emprestimo_editar'),
    path('deletar_emprestimo/<int:id>/',emprestimo_remover, name='emprestimo_remover'),

    #Autenticação
    path("logout/", desconectar, name="logout"),
    path('', autenticacao, name='login'),

    #Outros
    path('perfil/',perfil, name="perfil"),
    path('admin/', admin.site.urls),
    path('devolução/', devolucao, name="devolucao"),
    path('registro/', registro, name='registro'),

    #Usuario
    path('usuario_editar/<int:id>/', usuario_editar, name='usuario_editar'),
    path('usuario_listar/', usuario_listar, name='usuario_listar'),
    path('deletar_usuario/<int:id>/', usuario_remover, name='usuario_remover'),
]
