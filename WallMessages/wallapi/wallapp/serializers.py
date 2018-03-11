from rest_framework import serializers
from .models import Usuario, Disciplina, Disciplina_Alunos, Mensagem


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Usuario
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Disciplina
        fields = '__all__'
        depth = 1


class Disciplina_AlunosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Disciplina_Alunos
        fields = '__all__'
        depth = 1

class MensagemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Mensagem
        fields = '__all__'
