from django.test import TestCase
from procesamiento.models import Paciente

class PacienteModelTest(TestCase):
    def setUp(self):
        Paciente.objects.create(name="Juan Pérez", age=30, weight=70, height=175, cholesterol=190, heart_rate=80)

    def test_paciente_creation(self):
        paciente = Paciente.objects.get(name="Juan Pérez")
        self.assertEqual(paciente.age, 30)
