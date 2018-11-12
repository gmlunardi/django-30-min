from django.shortcuts import render
from .models import Produto

def home(request):
    nome = 'Django MOC' #passando variável para o template através de um dicionário
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'nome':nome, 'produtos':produtos})

def detalhe_produto(request, codigo):
    produto = Produto.objects.get(id=codigo)
    return render(request, 'produtos.html', {'produto':produto})