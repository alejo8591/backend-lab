from django.test import TestCase
from contacts.models import Contact

class ContactTest(TestCase):
	""" Contact models tests. """

	def test_str(self):

		contact = Contact(first_name='Alejandro', last_name='Romero')

		self.assertEquals(str(contact), 'Alejandro Romero', )