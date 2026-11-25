from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Pessoa


class PessoaViewsTests(TestCase):
    def setUp(self):
        self.pessoa = Pessoa.objects.create(
            nome='Pessoa de teste',
            nascimento=date(1990, 1, 1),
            cpf='12345678901',
            email='pessoa@example.com',
        )

    def test_pessoa_pages_render_with_namespaced_urls(self):
        paths = (
            reverse('pessoa:lista_pessoas'),
            reverse('pessoa:adicionar_pessoa'),
            reverse('pessoa:detalhar_pessoa', args=[self.pessoa.id]),
            reverse('pessoa:editar_pessoa', args=[self.pessoa.id]),
            reverse('pessoa:excluir_pessoa', args=[self.pessoa.id]),
        )

        for path in paths:
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)

    def test_missing_pessoa_returns_404(self):
        for name in ('detalhar_pessoa', 'editar_pessoa', 'excluir_pessoa'):
            with self.subTest(view=name):
                response = self.client.get(reverse(f'pessoa:{name}', args=[999]))
                self.assertEqual(response.status_code, 404)

    def test_redundant_list_route_is_removed(self):
        response = self.client.get('/pessoa/list/')
        self.assertEqual(response.status_code, 404)
