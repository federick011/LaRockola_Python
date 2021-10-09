from django.contrib import admin
from Usuarios.models import* #Importamod todos los modelos de nuestra app "Servicios"

# Register your models here.
admin.site.register(User)
admin.site.register(Perfil)
admin.site.register(Post)

