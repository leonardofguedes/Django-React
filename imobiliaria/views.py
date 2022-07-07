from rest_framework import generics
from .models import Imovel
from .serializers import ImovelSerializer

class ImovelView(generics.ListAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

