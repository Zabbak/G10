from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
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