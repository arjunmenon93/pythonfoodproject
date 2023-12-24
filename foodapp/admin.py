from django.contrib import admin

# Register your models here.
from . models import *
class catadmin(admin.ModelAdmin):
     prepopulated_fields={'slug':('name',)}
    
admin.site.register(categ,catadmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug','price','category','desc','img']
    list_editable=['price','desc','category','img']
admin.site.register(product,prodadmin)
