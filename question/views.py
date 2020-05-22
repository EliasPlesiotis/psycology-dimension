from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import AnonymousUser
from rest_framework import filters

from . import models, serializers

class questions(ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if not isinstance(user, AnonymousUser):
            return models.Question.objects.filter(user=user)
        else:
            return models.Question.objects.all()[:100]

class question(RetrieveUpdateDestroyAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [IsAuthenticated]

class question_read(RetrieveAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = []

class answer(CreateAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    permission_classes = []

class answer_read(RetrieveAPIView):
    queryset = models.Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = '__all__'