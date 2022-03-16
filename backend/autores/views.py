from rest_framework.viewsets import ModelViewSet

from .models import Autor
from .serializers import AutorSerializer

class AutoresViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer 

