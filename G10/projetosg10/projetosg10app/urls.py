from  django.urls import path
from . import views

urlpatterns = [
    path('', views.paginainicial, name='paginainicial'),
    path('apadrinhamento', views.apadrinhamento, name='apadrinhamento'),
    path('noticias', views.noticias, name='noticias'),
    path('cadastroelogin/', views.cadastroelogin, name='cadastroelogin'),
    path('administrador/', views.administrador, name='administrador'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('alunos', views.alunos, name='alunos'),
    path('cronograma', views.cronograma, name='cronograma'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('errologin', views.errologin, name='errologin'),
    path('setadm', views.setadm, name='setadm'),
    path('noticiaslog', views.noticiaslog, name='noticiaslog'),
    path('padrinhoslog', views.padrinhoslog, name='padrinhoslog'),
    path('apadrinhados', views.apadrinhados, name='apadrinhados'),
    
]