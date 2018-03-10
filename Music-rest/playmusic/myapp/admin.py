from django.contrib import admin
from .models import Music, Album, Band 
# Register your models here.

admin.site.register(Music)
admin.site.register(Band)
admin.site.register(Album)
