from django.contrib import admin
from .models.customuser_model import CustomUser

# Register your models here.
admin.site.register(CustomUser)
