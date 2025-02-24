import mock
from django.urls import reverse
#from django.test import TestCase, RequestFactory
from rest_framework.test import APITestCase

#from project_nevera_api.views import key_term_view
from project_nevera_api.services import Service

class KeyTermViewTestCase(APITestCase):
    @mock.patch.object(Service, 'get_key_terms', return_value=['Egg'])
    @mock.patch.object(Service, 'translate_array', return_value=[['Ou'], ['Huevo']])
    def test_initialize(self, mock_get_key_terms, mock_translate_array):
        url = '/keyterms/initialize/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.data, [{'eng': 'Egg', 'cat': 'Ou', 'esp': 'Huevo'}])