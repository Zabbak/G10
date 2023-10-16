from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render


# Create your views here.
def paginainicial(request):
    context = {
    }
    return render(request, 'paginicial.html', context)

def noticias(request):
    context = {
    }
    return render(request, 'noticias.html', context)

def apadrinhamento(request):
    context = {
    }
    return render(request, 'apadrinhamento.html', context)

def cadastroelogin(request):
    context = {
    }
    return render(request, 'cadastroelogin.html', context)

def cadastro(request):
    context = {
    }
    return render(request, 'cadastro.html', context)

def administrador(request):
    context = {
    }
    return render(request, 'administrador.html', context)

def alunos(request):
    context = {
    }
    return render(request, 'alunos.html', context)

def cronograma(request):
    context = {
    }
    return render(request, 'cronograma.html', context)

def usuarios(request):
    context = {
    }
    return render(request, 'usuarios.html', context)
