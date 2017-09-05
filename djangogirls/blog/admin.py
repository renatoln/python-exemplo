from django.contrib import admin
from .models import Post #importou o modelo anterior

admin.site.register(Post) #para tornar visível no site
