from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import AnonymousUser
from rest_framework import filters

from . import models, serializers


class questionnaires(ListCreateAPIView):
    serializer_class = serializers.QuestionnaireSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if not isinstance(user, AnonymousUser):
            return models.Questionnaire.objects.filter(user=user)
        else:
            return models.Questionnaire.objects.all()[:100]

class questionnaire_search(ListAPIView):
    queryset = models.Questionnaire.objects.all()
    serializer_class = serializers.QuestionnairePartialSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = []

class questionnaire(RetrieveUpdateDestroyAPIView):
    queryset = models.Questionnaire.objects.all()
    serializer_class = serializers.QuestionnaireSerializer
    permission_classes = [IsAuthenticated]

class questionnaire_read(RetrieveAPIView):
    queryset = models.Questionnaire.objects.all()
    serializer_class = serializers.QuestionnairePartialSerializer
    permission_classes = []