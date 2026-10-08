from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_medicos, name='lista_medicos'),
    path('adicionar/', views.adicionar_medico, name='adicionar_medico'),
    path('<int:id>/', views.detalhar_medico, name='detalhar_medico'),
    path('<int:id>/editar/', views.editar_medico, name='editar_medico'),
    path('<int:id>/excluir/', views.excluir_medico, name='excluir_medico'),
    
    path('especialidade/', views.lista_especialidades, name='lista_especialidades'),
    path('especialidade/adicionar/', views.adicionar_especialidade, name='adicionar_especialidade'),
    path('especialidade/<int:id>/', views.detalhar_especialidade, name='detalhar_especialidade'),
    path('especialidade/<int:id>/editar/', views.editar_especialidade, name='editar_especialidade'),
    path('especialidade/<int:id>/excluir/', views.excluir_especialidade, name='excluir_especialidade'),
]