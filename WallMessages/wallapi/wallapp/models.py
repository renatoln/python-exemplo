from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):

    id= models.AutoField(primary_key=True, blank=False, null=False)
    #username = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=50, unique=True, blank=False,)
    senha = models.TextField(blank=False, null=False)
    nome = models.CharField(max_length=250, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True) # 1 - professor; 2 - aluno

    def __str__(self):
        return self.nome + ' - ' + str(self.tipo)

    class Meta:
        db_table = 'usuario'


class Disciplina(models.Model):

    id = models.AutoField(primary_key=True, blank=False, null=False)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    professor = models.ForeignKey(Usuario, blank=True, null=False, related_name='data_professor')

    def __str__(self):
        return self.codigo  + ' - ' + self.nome  + ' - ' + self.professor.nome

    class Meta:
        db_table = 'disciplina'

class Disciplina_Alunos(models.Model):
    id =  models.AutoField(primary_key=True, blank=False, null=False)
    disciplina = models.ForeignKey(Disciplina, blank=False, null=False, related_name='data_disciplina')
    estudante = models.ForeignKey(Usuario, blank=False, null=False, related_name='data_estudante')
    #grade = models.IntegerField(null=True)
    #__table_args__ = (db.UniqueConstraint('course_section_id','user_id', name='course_section_user_uc'),)

    def __str__(self):
        return self.disciplina.nome + ' - ' + self.estudante.nome

    class Meta:
        db_table = 'disciplina_alunos'


class Mensagem(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    data = models.DateTimeField(null=True, default=timezone.now)
    remetente = models.ForeignKey(Usuario, blank=False, null=False, related_name='data_sender_who')
    destinatario = models.ManyToManyField(Usuario,blank=False, related_name='message_destinations')
    titulo = models.CharField(max_length=50, blank=False, null=False)
    texto = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'mensagem'
