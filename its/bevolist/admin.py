from django.contrib import admin
from bevolist.models import *

class CategoryAdmin(admin.ModelAdmin):
	list_display =['name']
	prepopulated_fields = {"slug" : ("name",)} 

class ItemAdmin(admin.ModelAdmin):
	list_display = ['name','category' ,'department', 'posted_on']
	list_filter = ['category', 'posted_on']

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)