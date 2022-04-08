from django.contrib import admin

# Register your models her
from administracion.models import Configuracion


@admin.register(Configuracion)
class PersonAdmin(admin.ModelAdmin):
    pass