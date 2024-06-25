from django.contrib import admin
from .models import *
from admin_confirm import AdminConfirmMixin
from django.contrib.admin import ModelAdmin

class PeriodistaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombre_completo', 'telefono','rut','habilitado']



# Register your models here.
admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Periodista, PeriodistaModelAdmin)


