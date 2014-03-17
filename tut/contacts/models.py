from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class Contact(models.Model):
	first_name = models.CharField(max_length=255,)
	last_name = models.CharField(max_length=255,)
	email = models.EmailField()

	def get_absolute_url(self):
		return reverse('contact-details', kwargs={'pk' : self.id})

	def __str__(self):
		return ' '.join([
			self.first_name,
			self.last_name,
		])

class Address(models.Model):
	contact = models.ForeignKey(Contact)
	address_type = models.CharField(max_length=60)
	adress = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=4)
	postal_code = models.CharField(max_length=20)

	class Meta:
		unique_together = ('contact', 'address_type',)
