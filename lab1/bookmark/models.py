from django.db import models
#from django.utils.encoding import python_2_unicode_compatible

# https://docs.djangoproject.com/en/1.7/topics/python3/#str-and-unicode-methods
#@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

#@python_2_unicode_compatible
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
