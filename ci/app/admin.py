from django.contrib import admin
from app.models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug' : ("name",)}

class ItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'department', 'posted_on']
	list_filter = ['category', 'posted_on']

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)