from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("editar/", views.editar, name="editar"),
    path("apagar/", views.apagar, name="apagar"),
    path("listar/", views.listar, name="listar"),
]