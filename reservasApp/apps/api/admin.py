from django.contrib import admin
from .models.client_model import Client

# define how to show the models in admin modul

class ClientAdmin(admin.ModelAdmin):
    verbose_name = 'Clent'
    verbose_name_plural = 'Clents'
    ordering = ['full_name']
    list_display = ('full_name', 'doc_type', 'doc', 'phone')
    search_fields = ('full_name', 'doc')


# Register the models.
admin.site.register(Client, ClientAdmin)
