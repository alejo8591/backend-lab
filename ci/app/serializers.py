from rest_framework import serializers

from app.models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Category
		fields = ('url', 'name', 'slug',)