from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from ..serializers import KeyTermSerializer
from ..models import KeyTerm
from project_nevera_api.services import Service

class KeyTermViewset(viewsets.ModelViewSet):
    queryset = KeyTerm.objects.all()
    serializer_class = KeyTermSerializer
    service = Service()

    def get_queryset(self):
        return KeyTerm.objects.all()
    
    @action(methods=['get'], detail=False)
    def initialize(self, request):
        key_terms = self.get_queryset()
        if len(key_terms) == 0:
            response = self.service.get_key_terms()
            translations = self.service.translate_array(response)
            for i, item in enumerate(response):
                ca_translation = None
                es_translation = None
                if i < len(translations[0]):
                    ca_translation = translations[0][i]
                if i < len(translations[1]):
                    es_translation = translations[1][i]
                KeyTerm.objects.create(eng=item, cat=ca_translation, esp=es_translation)
            key_terms = self.get_queryset()
        serializer = self.serializer_class(key_terms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)