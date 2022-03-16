from dataclasses import field
from rest_framework.serializers import ModelSerializer

from .models import Autor

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome', 'tema', 'texto']