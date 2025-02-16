from django.test import TestCase
from project_nevera_api.services import Service
import responses

class ServiceTestCase(TestCase):
    def setUp(self):
        self.service = Service()

    @responses.activate
    def test_get_key_terms(self):
        expected_response = {
            "batchcomplete":"",
            "limits": {
                "categorymembers":500
            },
            "query": {
                "pages": {
                    "22836": {
                        "pageid":22836,
                        "ns":102,
                        "title":"Cookbook:Pecorino Romano Cheese"
                    }
                }
            }
        }

        api_url = self.service.WIKIMEDIA_INGREDIENTS_API_URL

        responses.add(
            responses.GET,
            api_url,
            json=expected_response,
            status=200,
            content_type='application/json'
        )

        response = self.service.get_key_terms()

        self.assertEqual(response, ["Pecorino Romano Cheese"])
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, api_url)