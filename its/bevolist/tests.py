from django.test import TestCase
from bevolist.models import *

class TestBevolist(TestCase):

	def setUp(self):
		self.cat1 = Category.objects.create(name="Hardware", slug="hardware")
		self.cat2 = Category.objects.create(name="Software", slug="software")
		self.cat3 = Category.objects.create(name="Misc. Hardware", slug="misc-hardware")
		self.item1 = Item.objects.create(listing="T", name="Computers", category=self.cat1, department="ITS", description="Dell computers.")
		self.item2 = Item.objects.create(listing="T", name="Servers", category=self.cat1, department="ITS", description="Dell servers.")
		self.item3 = Item.objects.create(listing="L", name="Adobe", category=self.cat2, department="HR", description="Acrobat.")
		self.item4 = Item.objects.create(listing="T", name="Matlab", category=self.cat2, department="HR", description="Crunch Numbers.")
		self.item5 = Item.objects.create(listing="T", name="Quake", category=self.cat2, department="ITS", description="Get your game on.")

	def test_category_urls(self):
		response = self.client.get('/bevolist/category/')
		self.assertEqual(response.status_code, 200)
		response = self.client.get('/bevolist/category/bless/')
		self.assertEqual(response.status_code, 404)