from django.contrib import admin
from .models import BrandModel
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('Brand_Name',)}
    list_display=('Brand_Name','slug')
    
admin.site.register(BrandModel,BrandAdmin)
