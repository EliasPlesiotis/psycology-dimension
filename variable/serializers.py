from rest_framework import serializers

from . import models
from question.serializers import QuestionSerializer, AnswerSerializer


class VariableSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = models.Variable
        fields = '__all__'

class VariablePartialSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = models.Variable
        fields = ['id', 'name']