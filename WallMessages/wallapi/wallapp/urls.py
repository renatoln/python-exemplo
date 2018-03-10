from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^usuarios/$', views.UsuarioList.as_view(), name='usuario-list'),
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view(), name='usuario-detail'),

    url(r'^disciplinas/$', views.DisciplinaList.as_view()),
    url(r'^disciplina/(?P<pk>[0-9]+)/$', views.DisciplinaDetail.as_view()),

    url(r'^disciplina_alunoss/$', views.Disciplina_AlunosList.as_view()),
    url(r'^disciplina_alunos/(?P<pk>[0-9]+)/$', views.Disciplina_AlunosDetail.as_view()),


    url(r'^mensagens/$', views.MensagemList.as_view()),
    url(r'^mensagem/(?P<pk>[0-9]+)/$', views.MensagemDetail.as_view()),
    
]
