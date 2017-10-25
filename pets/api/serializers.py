from rest_framework import serializers
from ..models import *


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ["name", "birthday", "animal_kind"]
