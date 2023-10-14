from django.urls import path

from . import views

urlpatterns = [
    path("", views.paginainicial, name="paginainicial"),
    path("apadrinhamento", views.apadrinhamento, name="apadrinhamento"),
]