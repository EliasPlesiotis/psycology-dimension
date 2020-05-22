from django.db import models
from django.contrib.auth.models import User
import uuid

from questionnaire.models import Questionnaire

class Variable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='varibles')
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='variables')

    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name