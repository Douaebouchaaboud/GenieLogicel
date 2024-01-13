 # Register your models here.
from django.contrib import admin
from appointements.models import Appoi 

@admin.register(Appoi)
class AppoiAdmin(admin.ModelAdmin):
    list_display = ('aid', 'NomClient', 'EmailC', 'TypeMar', 'Comment', 'dateApp')
    search_fields = ['NomClient', 'EmailC']  # Add any fields you want to be searchable in the admin
    list_filter = ['TypeMar', 'dateApp']  # Add any fields you want to use as filters in the admin
    ordering = ['-dateApp']  # Default ordering based on dateApp

