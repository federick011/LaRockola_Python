from django.contrib import admin
from Servicios.models import * #Importamod todos los modelos de nuestra app "Servicios"

# Register your models here.
admin.site.register(Musico)
admin.site.register(GeneroMusical)
admin.site.register(Album)
admin.site.register(Canciones)
admin.site.register(Playlist)
