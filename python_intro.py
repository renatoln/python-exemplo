def ola(nome):
	print('Ola '+ nome)


girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
if 5 > 2 and False: #True
	print ("maior")
	for i in range(1, 6):
		print(i)

else:
	print("menor")
	for n in girls:
		ola(n)


# criar virtualenv com conda
# > conda create -n yourenvname python=x.x anaconda

# iniciar a virtualevn anaconda
# > source activate renatoenv
# parar
# > source deactivate

# instalando o DJango dentro da virtualenv
# (myvenv) ~$ pip install django==1.8.5 whitenoise==2.0
# congelar versões do Django
# (myvenv) ~$ pip freeze > requirements.txt

# PARA INICIALIZAR UM PROJETO NOVO
# > django-admin startproject mysite .
# manage.py é um script que ajuda com a gestão do site.
# settings.py contém a configuração do seu site.
# urls.py contém uma lista dos padrões usados por urlresolver.

# criar uma app dentro do site (nome = blog)
# > python manage.py startapp blog

# dizer ao django para usar a app
# em settings.py addicione a app blog

# em APP/models.py adicionar os models
# após isso
# python manage.py makemigrations blog
# python manage.py migrate blog
# adicionar os models em blog/admin.py
# cria views em blog/views.py
# adiciona os templates em blog/templates/blog

# cofigura urls.py e blog/urls.py para setar urls


# PARA INSTALAR UM PROJETO JA EXISTENTE
#instalar as depedencia do projeto
# > pip install -r requeriments.txt

#criar a base
# > python manage.py migrate
# migrate -> cria scripts e tabelas na primeira vez
# > python manage.py makemigrations
# makemigrations -> depois da primeira vez, só gera os scripts

#criar super user
# > python manage.py createsuperuser

#rodar o servidor
# > python manage.py runserver

# root -> admin123
