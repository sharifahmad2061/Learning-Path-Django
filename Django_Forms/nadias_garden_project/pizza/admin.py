from django.contrib import admin
from .models import Pizza, Size


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['topping1', 'topping2', 'size']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass
