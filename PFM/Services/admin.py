from django.contrib import admin
from .models import CatererService, ImageCar, MakeupService, Image , DjsServices , ImageDjs

class ImageInline(admin.TabularInline):  
    model = Image
    extra = 3  

class MakeupServiceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'introduction', 'address', 'ville', 'rating', 'price_per_hour')
    search_fields = ['name', 'ville']  
    list_filter = ['ville', 'rating']  

admin.site.register(MakeupService, MakeupServiceAdmin)

#Djs 
class ImageInline(admin.TabularInline): 
    model = ImageDjs
    extra = 1 

class DjsAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'introduction', 'address', 'ville', 'rating', 'price_per_hour')
    search_fields = ['name', 'ville']  
    list_filter = ['ville', 'rating']  


admin.site.register(DjsServices, DjsAdmin)

#Traiteur
class ImageInline(admin.TabularInline):
    model = ImageCar
    extra = 3

class CatererServiceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'introduction', 'address', 'ville', 'rating', 'price_per_Table')
    search_fields = ['name', 'ville']
    list_filter = ['ville', 'rating']

admin.site.register(CatererService, CatererServiceAdmin)
