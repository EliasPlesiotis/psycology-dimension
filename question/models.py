from django.db import models
from django.contrib.auth.models import User
import uuid

from variable.models import Variable
from questionnaire.models import Questionnaire

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE, related_name='questions')
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='questions')

    body = models.TextField()
    
class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.CharField(max_length=64)
    gender = models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=50)
    age = models.IntegerField()
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], blank=True)