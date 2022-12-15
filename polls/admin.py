from django.contrib import admin
from . import models


@admin.register(models.Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_by', 'pub_date']


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'choice_text']
