from django.contrib import admin

# Register your models here.

from .models import User, Apartamentos, Estadisticas

admin.site.register(User)
admin.site.register(Apartamentos)
admin.site.register(Estadisticas)

