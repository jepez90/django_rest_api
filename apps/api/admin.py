from django.contrib import admin

from .models.reserve_model import Reserve
from .models.client_model import Client

# define how to show the models in admin modul


class ClientAdmin(admin.ModelAdmin):
    verbose_name = 'Clent'
    verbose_name_plural = 'Clents'
    ordering = ['full_name']
    list_display = ('full_name', 'doc_type', 'doc', 'phone')
    search_fields = ('full_name', 'doc')


class ReserveAdmin(admin.ModelAdmin):
    ordering = ['date', 'hour']
    list_display = ('plate', 'date', 'hour', 'owner', 'driver')
    search_fields = ('plate', 'owner', 'driver')


# Register the models.
admin.site.register(Client, ClientAdmin)
admin.site.register(Reserve, ReserveAdmin)
