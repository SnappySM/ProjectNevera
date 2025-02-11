from django.test import TestCase
from project_nevera_api.models import KeyTerm

class KeyTermTestCase(TestCase):
    def setUp(self):
        KeyTerm.objects.create(eng="egg", cat="ou", esp="huevo")

    def test_key_term_creation(self):
        keyTerm = KeyTerm.objects.get(eng="egg")
        self.assertEqual(keyTerm.cat, "ou")
        self.assertEqual(keyTerm.esp, "huevo")