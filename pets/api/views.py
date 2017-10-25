from rest_framework.permissions import (
    IsAuthenticated,
    )

from rest_framework import viewsets
from ..models import Pet
from .serializers import PetSerializer
from .permissions import IsOwner


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        qs = Pet.objects.filter(owner=user)
        return qs