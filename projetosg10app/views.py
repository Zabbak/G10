from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .models import Usuarios


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
    
    return render(request, 'administrador.html')

def alunos(request):
    context = {
    }
    return render(request, 'alunos.html', context)

def cronograma(request):
    context = {
    }
    return render(request, 'cronograma.html', context)

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        email = request.POST.get('email')

        if nome and senha:
            usuario = Usuarios(nome=nome, senha=senha, email=email)
            usuario.save()

            return redirect('administrador')
        
    usuarios = Usuarios.objects.all()
    return render(request, 'cadastro.html', {'usuarios': usuarios})
