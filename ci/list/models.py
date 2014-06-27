from django.db import models

L_TYPES = (
	('t', 'Para publicar'),
	('l', 'Buscando respuesta'),
)

class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)

	def __unicode__(self):
		return "%s - %s" % (self.name, self.slug)

class Item(models.Model):
	listing = models.CharField(max_length=1, choices=L_TYPES, default='t')
	name = models.CharField(max_length=255)
	category = models.ForeignKey(Category)
	department = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	posted_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s - %s - %s - %s" % (self.name, self.listing, self.category, self.department)

class Picture(models.Model):
	item = models.ForeignKey(Item)
	url = models.CharField(max_length=255)