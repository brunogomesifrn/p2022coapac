from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def emprestimo(request):
    return render(request, 'emprestimo.html')

def devolucao(request):
    return render(request, 'devolucao.html')

def listar(request):
    return render(request, 'listar.html')

def novo(request):
    return render(request, 'novo.html')
