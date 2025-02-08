from django.test import TestCase
from project_nevera_api.models import Refrigerator

class RefrigeratorTestCase(TestCase):
    def setUp(self):
        self.testRefigerator = Refrigerator.objects.create(name="TestRefrigerator", description="This is a test refrigerator")

    def test_refrigerator_creation(self):
        refrigerator = Refrigerator.objects.get(id=self.testRefigerator.id)
        self.assertEqual(refrigerator.name, "TestRefrigerator")
        self.assertEqual(refrigerator.description, "This is a test refrigerator")