from rest_framework import serializers
from .models import Elon_Baza

class ElonBazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elon_Baza
        fields = '__all__'
