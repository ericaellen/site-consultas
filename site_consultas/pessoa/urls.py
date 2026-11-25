from django.urls import path

from . import views

app_name = 'pessoa'

urlpatterns = [
    path('', views.lista_pessoas, name='lista_pessoas'),
    path('adicionar/', views.adicionar_pessoa, name='adicionar_pessoa'),
    path('<int:id>/', views.detalhar_pessoa, name='detalhar_pessoa'),
    path('<int:id>/editar/', views.editar_pessoa, name='editar_pessoa'),
    path('<int:id>/excluir/', views.excluir_pessoa, name='excluir_pessoa'),
]