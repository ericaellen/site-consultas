from datetime import date, datetime

from django.test import TestCase
from django.urls import reverse

from medico.models import Medico
from pessoa.models import Pessoa
from .models import Consulta


class ConsultaViewsTests(TestCase):
    def setUp(self):
        self.pessoa = Pessoa.objects.create(
            nome='Paciente de teste',
            nascimento=date(1990, 1, 1),
            cpf='12345678901',
            email='paciente@example.com',
        )
        self.medico = Medico.objects.create(
            nome='Médico de teste',
            nascimento=date(1980, 1, 1),
            cpf='12345678902',
            email='medico@example.com',
            crm='CRM-TESTE',
        )
        self.consulta = Consulta.objects.create(
            dataHora=datetime(2025, 1, 1, 10, 0),
            status='agendada',
            pessoa=self.pessoa,
            medico=self.medico,
        )

    def test_consulta_string_representation(self):
        self.assertEqual(
            str(self.consulta),
            'Consulta de Paciente de teste com Médico de teste em 01/01/2025 10:00',
        )

    def test_consulta_pages_render_with_namespaced_urls(self):
        paths = (
            reverse('consulta:lista_consultas'),
            reverse('consulta:adicionar_consulta'),
            reverse('consulta:detalhar_consulta', args=[self.consulta.id]),
            reverse('consulta:editar_consulta', args=[self.consulta.id]),
            reverse('consulta:excluir_consulta', args=[self.consulta.id]),
        )

        for path in paths:
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)

    def test_missing_consulta_returns_404(self):
        for name in ('detalhar_consulta', 'editar_consulta', 'excluir_consulta'):
            with self.subTest(view=name):
                response = self.client.get(reverse(f'consulta:{name}', args=[999]))
                self.assertEqual(response.status_code, 404)

    def test_redundant_list_route_is_removed(self):
        response = self.client.get('/consulta/list/')
        self.assertEqual(response.status_code, 404)
