from django.test import TestCase
from django.urls import reverse


class ViewsNotFoundTests(TestCase):
    def test_list_pages_render_with_namespaced_urls(self):
        for name in ('lista_medicos', 'lista_especialidades'):
            with self.subTest(view=name):
                response = self.client.get(reverse(f'medico:{name}'))
                self.assertEqual(response.status_code, 200)

    def test_missing_medico_returns_404(self):
        for name in ('detalhar_medico', 'editar_medico', 'excluir_medico'):
            with self.subTest(view=name):
                response = self.client.get(reverse(f'medico:{name}', args=[999]))
                self.assertEqual(response.status_code, 404)

    def test_missing_especialidade_returns_404(self):
        for name in (
            'detalhar_especialidade',
            'editar_especialidade',
            'excluir_especialidade',
        ):
            with self.subTest(view=name):
                response = self.client.get(reverse(f'medico:{name}', args=[999]))
                self.assertEqual(response.status_code, 404)
