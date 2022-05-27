from xml.etree.ElementPath import prepare_child
from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)} 
    list_display = ('category_name', 'slug')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
