from rest_framework import generics
from .models import Elon_Baza
from .serializers import ElonBazaSerializer

class ElonBazaListView(generics.ListAPIView):
    queryset = Elon_Baza.objects.all()
    serializer_class = ElonBazaSerializer
