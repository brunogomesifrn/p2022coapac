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
import imp
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from apps.core.views import emprestimo, devolucao, listar, novo, perfil


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('perfil/',perfil, name="perfil"),
    path('admin/', admin.site.urls),
    path('emprestimo/',emprestimo, name="emprestimo"),
    path('devolução/', devolucao, name="devolucao"),
    path('listar/', listar, name="listar"),
    path('novo/', novo, name="novo"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
