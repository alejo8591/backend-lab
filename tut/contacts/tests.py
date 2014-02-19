from django.test import TestCase
from django.test.client import Client, RequestFactory
from contacts.models import Contact
from contacts.views import *

class ContactTest(TestCase):
	""" Contact models tests. """

	def test_str(self):

		contact = Contact(first_name='Alejandro', last_name='Romero')

		self.assertEquals(str(contact), 'Alejandro Romero', )

class ContactListViewTest(TestCase):
	""" Contact list view test """
	def test_contacts_in_the_context(self):
		client = Client()
		response = client.get('/')

		self.assertEquals(list(response.context['object_list']), [])

		Contact.objects.create(first_name='Camilo', last_name='forro')

		response = client.get('/')
		self.assertEquals(response.context['object_list'].count(), 1)

	def test_contact_in_the_context_request_factory(self):
		factory = RequestFactory()
		request = factory.get('/')

		response = ListContactView.as_view()(request)

		self.assertEquals(list(response.context_data['object_list']), [])

		Contact.objects.create(first_name='Pam', last_name='Per')
		response = ListContactView.as_view()(request)
		self.assertEquals(response.context_data['object_list'].count(), 1)
