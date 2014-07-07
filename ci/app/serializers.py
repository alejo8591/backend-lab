from rest_framework import serializers

from app.models import Category, Item

class CategorySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Category
		fields = ('url', 'name', 'slug',)

class ItemSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Item 
		fields = ('listing', 'name', 'category', 'department', 'description', 'update_item',)