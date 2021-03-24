from django.contrib import admin
from .models import Post

#Isso significa que estamos importando do "moldels.py" a classe Post que foi criada
# Register your models here.
admin.site.register(Post)