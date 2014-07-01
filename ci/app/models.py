from django.db import models

L_TYPES = (
    ('t', 'Para resolver'),
	('l', 'Para revisar'),
	('p', 'No resuelto'),
)

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
		return "%s - %s" % (self.name, self.slug)

class Item(models.Model):
    listing = models.CharField(max_length=1, choices=L_TYPES, default='T')
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    department = models.CharField(max_length=255)
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    update_item = models.DateTimeField()

    def __unicode__(self):
		return "%s - %s - %s - %s - %s" % (self.name, self.category, self.department, self.description, self.update_item)

class Picture(models.Model):
    item = models.ForeignKey(Item)
    url = models.CharField(max_length=255)