from django.db import models
from django.contrib.auth.models import User
import uuid


class Questionnaire(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questionnaires')
    name = models.CharField(max_length=40)
    desc = models.TextField()

    def __str__(self):
        return self.name