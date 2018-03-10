from django.contrib import admin
from .models import Usuario, Disciplina, Disciplina_Alunos, Mensagem

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Disciplina)
admin.site.register(Disciplina_Alunos)
admin.site.register(Mensagem)
