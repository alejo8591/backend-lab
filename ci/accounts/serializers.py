from rest_framework import serializers

from django.contrib.auth.models import User

from accounts.models import UserProfile

class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'first_name', 'last_name',)

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = UserProfile
		fields = ('url', 'user', 'website',)