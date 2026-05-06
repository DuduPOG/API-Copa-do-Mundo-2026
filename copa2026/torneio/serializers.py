from rest_framework import serializers
from .models import Grupo, Selecao, Jogador, Jogo, EventoJogo, Tecnico

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'     

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'
             
class SelecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selecao
        fields = '__all__'     

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'     

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'     

class EventoJogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoJogo
        fields = '__all__'     
