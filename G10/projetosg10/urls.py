from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("projetosg10app.urls")),
    path("admin/", admin.site.urls),
]