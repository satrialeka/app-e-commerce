from django.contrib import admin 
from .models import Sneakers

class SneakersAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'quantity')

admin.site.register(Sneakers, SneakersAdmin)
