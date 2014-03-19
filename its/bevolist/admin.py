from django.contrib import admin
from bevolist.models import *

class CategoryAdmin(admin.ModelAdmin):
	pass

class ItemAdmin(admin.ModelAdmin):
	pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)