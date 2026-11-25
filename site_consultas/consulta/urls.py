from django.urls import path

from . import views

app_name = 'consulta'

urlpatterns = [
    path('', views.lista_consultas, name='lista_consultas'),
    path('adicionar/', views.adicionar_consulta, name='adicionar_consulta'),
    path('<int:id>/', views.detalhar_consulta, name='detalhar_consulta'),
    path('<int:id>/editar/', views.editar_consulta, name='editar_consulta'),
    path('<int:id>/excluir/', views.excluir_consulta, name='excluir_consulta'),
]