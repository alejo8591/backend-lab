# -*- coding:utf-8 -*-
from django.test import TestCase
from app.models import Category, Item
from datetime import datetime

from django.utils.timezone import utc

class TestCidei(TestCase):
	def setUp(self):
		self.cat_one = Category.objects.create(name="Hardware", slug="hardware")
		self.cat_two = Category.objects.create(name="Software", slug="software")
		self.item_one = Item.objects.create(listing="t", name="Computers", category=self.cat_one, department="Electronics", description="lalalala", update_item=datetime.utcnow().replace(tzinfo=utc))
		self.item_two = Item.objects.create(listing="p", name="Servers", category=self.cat_one, department="Electronics",description="lololol", update_item=datetime.utcnow().replace(tzinfo=utc))
		self.item_three = Item.objects.create(listing="t", name="Cidei", category=self.cat_two, department="Systems", description="ffkffkfkfkf", update_item=datetime.utcnow().replace(tzinfo=utc))
		self.item_four = Item.objects.create(listing="p", name="Web", category=self.cat_two, department="Marketing",description="fgjdflsgjdlsgldsg", update_item=datetime.utcnow().replace(tzinfo=utc))

	def test_cat_one(self):
		response = self.client.get('/categories/%s/' % self.cat_one.slug)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Hardware')

	def test_item_one(self):
		response = self.client.get('/items/%s/' % self.item_one.id)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Computers')

	def test_item_two(self):
		response = self.client.get('/items/%s/' % self.item_two.id)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Servers')

	def test_item_three(self):
		response = self.client.get('/items/%s/' % self.item_three.id)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Cidei')

	def test_item_four(self):
		response = self.client.get('/items/%s/' % self.item_four.id)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Web')