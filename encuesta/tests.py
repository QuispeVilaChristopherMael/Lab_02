from django.test import TestCase, Client
from django.urls import reverse

class EncuestaLabTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_formulario_encuesta_get(self):
        response = self.client.get(reverse('encuesta:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Formulario")
        self.assertContains(response, "name=\"nombre\"")

    def test_enviar_encuesta_post(self):
        data = {
            'nombre': 'Juan Perez',
            'password': 'secretpassword',
            'educacion': 'universidad',
            'nacionalidad': 'hispana',
            'idiomas': ['español', 'inglés'],
            'email': 'juan@example.com',
            'sitioweb': 'https://example.com'
        }
        response = self.client.post(reverse('encuesta:enviar'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Respuesta")
        self.assertContains(response, "Juan Perez")
        self.assertContains(response, "universidad")
        self.assertContains(response, "español")
        self.assertContains(response, "inglés")
        self.assertContains(response, "juan@example.com")
        self.assertContains(response, "https://example.com")

    def test_operaciones_get(self):
        response = self.client.get(reverse('encuesta:operaciones'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Operaciones Matemáticas")

    def test_operaciones_suma(self):
        data = {'num1': '18', 'num2': '19', 'operacion': 'suma'}
        response = self.client.post(reverse('encuesta:calcular_operacion'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "La suma de 18 + 19 = 37")

    def test_operaciones_resta(self):
        data = {'num1': '25', 'num2': '10', 'operacion': 'resta'}
        response = self.client.post(reverse('encuesta:calcular_operacion'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "La resta de 25 - 10 = 15")

    def test_operaciones_multiplicacion(self):
        data = {'num1': '4', 'num2': '5', 'operacion': 'multiplicacion'}
        response = self.client.post(reverse('encuesta:calcular_operacion'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "La multiplicación de 4 * 5 = 20")

    def test_cilindro_get(self):
        response = self.client.get(reverse('encuesta:cilindro'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CÁLCULO DEL VOLUMEN DE UN CILINDRO")

    def test_cilindro_calculo(self):
        data = {'diametro': '2,15', 'altura': '1,75'}
        response = self.client.post(reverse('encuesta:calcular_cilindro'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "El volumen del cilindro es de 6.35338096859 metros cúbicos")
