from django.contrib import admin

from .models import Paciente, Cama, Planta

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Cama)
admin.site.register(Planta)
