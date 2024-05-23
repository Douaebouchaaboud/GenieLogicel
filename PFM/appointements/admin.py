 # Register your models here.
from django.contrib import admin
from appointements.models import Appoi 

class AppoiAdmin(admin.ModelAdmin):
    list_display = ('aid', 'NomClient', 'EmailC', 'TypeMar', 'Comment', 'dateApp')
    search_fields = ['NomClient', 'EmailC']  
    list_filter = ['TypeMar', 'dateApp']  
    ordering = ['-dateApp']  

admin.site.register(Appoi, AppoiAdmin)

