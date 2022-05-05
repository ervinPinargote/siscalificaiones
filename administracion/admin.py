from django.contrib import admin

# Register your models her
from administracion.models import Configuracion, calificacion_parametros, candidatas, parametros, certamen, \
    usuario_calificador, parametros_certamen, metricas_parametros


@admin.register(Configuracion)
class ConfiguracionAdmin(admin.ModelAdmin):
    pass



@admin.register(certamen)
class certamenAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_certamen")
    search_fields = ('nombre_certamen',)


@admin.register(parametros)
class parametrosAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_parametro")
    search_fields = ('nombre_parametro',)

@admin.register(candidatas)
class candidatasAdmin(admin.ModelAdmin):
    list_display = ("id", "cedula", "nombres","apellidos", "edad", "representa")
    search_fields = ('cedula', 'nombres', 'apellidos', 'edad', 'representa')

@admin.register(calificacion_parametros)
class calificacion_parametrosAdmin(admin.ModelAdmin):
    list_display = ("id", "id_candidata", "id_parametro", "id_usuario", "calificacion")
    search_fields = ('cedula', 'id_candidata__nombres', 'id_parametro__nombre_parametro', 'id_usuario__username')

@admin.register(usuario_calificador)
class usuario_calificadorAdmin(admin.ModelAdmin):
    list_display = ("id", "id_certamen", "id_usuario")
    search_fields = ('cedula', 'id_certamen__nombre_certamen', 'id_usuario__username')

@admin.register(parametros_certamen)
class parametros_certamenAdmin(admin.ModelAdmin):
    list_display = ("id", "id_certamen", "id_parametro")
    search_fields = ('id_certamen__nombre_certamen', 'id_parametro__nombre_parametro')

@admin.register(metricas_parametros)
class metricas_parametrosAdmin(admin.ModelAdmin):
    list_display = ("id", "nombremetrica", "puntacionmax", "idparametrof")
    search_fields = ('nombremetrica', 'idparametrof__nombre_parametro')