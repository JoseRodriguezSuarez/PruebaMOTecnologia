from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields=('id','nPok', 'nombre', 'peso', 'altura', 'cadEvolutiva', 'hp', 'special_attack', 'special_defense', 'speed', 'nivelEvolutivo')