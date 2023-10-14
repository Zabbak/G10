from django.urls import path

from . import views

urlpatterns = [
    path("", views.paginainicial, name="paginainicial"),
    path("apadrinhamento", views.apadrinhamento, name="apadrinhamento"),
    path("noticias", views.apadrinhamento, name="noticias"),
    path("cadastroelogin", views.apadrinhamento, name="cadastroelogin"),
    path("cadastro", views.apadrinhamento, name="cadastro"),
    path("administrador", views.apadrinhamento, name="administrador"),
]