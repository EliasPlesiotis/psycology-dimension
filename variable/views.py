from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser

from . import models, serializers


class variables(ListCreateAPIView):
    serializer_class = serializers.VariableSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not isinstance(user, AnonymousUser):
            return models.Variable.objects.filter(user=user)
        else:
            return models.Variable.objects.all()[:100]

class variable(RetrieveUpdateDestroyAPIView):
    queryset = models.Variable.objects.all()
    serializer_class = serializers.VariableSerializer
    permission_classes = [IsAuthenticated]