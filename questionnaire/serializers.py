from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Questionnaire
from question.serializers import QuestionSerializer, AnswerSerializer
from variable.serializers import VariablePartialSerializer

class QuestionnaireSerializer(ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    variables = VariablePartialSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Questionnaire
        fields = '__all__'

class QuestionnairePartialSerializer(ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    variables = VariablePartialSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Questionnaire
        fields = '__all__'