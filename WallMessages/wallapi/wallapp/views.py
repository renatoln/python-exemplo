#from django.shortcuts import render
# Create your views here.

from .models import Usuario, Disciplina, Disciplina_Alunos, Mensagem
from .serializers import UsuarioSerializer, DisciplinaSerializer, Disciplina_AlunosSerializer, MensagemSerializer
from rest_framework import generics
#from rest_framework.authentication import SessionAuthentication
#from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


class UsuarioList(generics.ListCreateAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )


class DisciplinaList(generics.ListCreateAPIView):

    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )


class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )


class Disciplina_AlunosList(generics.ListCreateAPIView):

    queryset = Disciplina_Alunos.objects.all()
    serializer_class = Disciplina_AlunosSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )


class Disciplina_AlunosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina_Alunos.objects.all()
    serializer_class = Disciplina_AlunosSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )


class MensagemList(generics.ListCreateAPIView):

    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )


class MensagemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
