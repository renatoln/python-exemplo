#from django.shortcuts import render
# Create your views here.

from .models import Usuario, Disciplina, Disciplina_Alunos, Mensagem
from .serializers import UsuarioSerializer, DisciplinaSerializer, Disciplina_AlunosSerializer, MensagemSerializer
from rest_framework import generics
from django_filters import rest_framework as filters
#from rest_framework.authentication import SessionAuthentication
#from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

'''
class UsuarioFilter(filters.FilterSet):

    email = filters.DateFilter(name="date", lookup_expr='gte')
    senha = filters.DateFilter(name="date", lookup_expr='lte')

    class Meta:

        model = Usuario
        fields = '__all__'
'''
class UsuarioList(generics.ListCreateAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    #filter_class = UsuarioFilter


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class DisciplinaList(generics.ListCreateAPIView):

    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class Disciplina_AlunosList(generics.ListCreateAPIView):

    queryset = Disciplina_Alunos.objects.all()
    serializer_class = Disciplina_AlunosSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class Disciplina_AlunosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina_Alunos.objects.all()
    serializer_class = Disciplina_AlunosSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class MensagemList(generics.ListCreateAPIView):

    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class MensagemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
