from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)

LISTING_TYPES  = (
		('T', 'For trade or disposal'),
		('L', 'looking for item'),
	)

class Item(models.Model):
	listing = models.CharField(max_length=1, choices=LISTING_TYPES, default='T')
	name = models.CharField(max_length=255)
	category = models.ForeignKey(Category)
	department = models.CharField(max_length=255)
	description = models.TextField()
	posted_on = models.DateTimeField(auto_now_add=True)