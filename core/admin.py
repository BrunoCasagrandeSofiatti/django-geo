from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from persons.models import Person

@register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ('name', 'first_name', 'last_name', 'age')
    name = 'persons'
    icon_name = 'person_pin'