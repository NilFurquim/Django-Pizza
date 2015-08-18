from django.contrib import admin

from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ingridients']
    list_display = ['name', 'ingridients']

admin.site.register(Pizza, PizzaAdmin)