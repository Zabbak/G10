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
def errologin(request):
    return render(request, 'errologin.html')

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
        tipologin = request.POST.get('tipologin')

        if nome and senha:
            usuario = Usuarios(nome=nome, senha=senha, email=email, tipologin=tipologin)
            usuario.save()

            return redirect('cadastroelogin')
        
    usuarios = Usuarios.objects.all()
    return render(request, 'cadastro.html', {'usuarios': usuarios})

def cadastroelogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if email and senha:
            try:
                usuario = Usuarios.objects.get(email=email, senha=senha)
                return redirect('administrador')

            except Usuarios.DoesNotExist:
                # Usuário não encontrado, ou senha incorreta
                error_message = "Nome de usuário ou senha incorretos."
                return render(request, 'errologin.html', {'error_message': error_message})

    return render(request, 'cadastroelogin.html')

def setadm(request):
    context = {
    }
    return render(request, 'setadm.html', context)

def noticiaslog(request):
    context = {
    }
    return render(request, 'noticiaslog.html', context)
def padrinhoslog(request):
    context = {
    }
    return render(request, 'padrinhoslog.html', context)
