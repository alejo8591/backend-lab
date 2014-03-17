from django.test import TestCase, LiveServerTestCase
from django.test.client import Client, RequestFactory
from contacts.models import Contact
from contacts.views import *
from selenium.webdriver.firefox.webdriver import WebDriver
from rebar.testing import flatten_to_dict
from contacts.forms import ContactForm

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


class ContactListIntegrationTests(LiveServerTestCase):

	@classmethod
	def setUpClass(cls):
		cls.selenium = WebDriver()
		super(ContactListIntegrationTests, cls).setUpClass()

	@classmethod
	def tearDownClass(cls):
		cls.selenium.quit()
		super(ContactListIntegrationTests, cls).tearDownClass()

	def test_contact_listed(self):
		#create a test contact
		Contact.objects.create(first_name='Alejandro', last_name='Romero')

		# make sure it's listed as <first> <last> on the list
		self.selenium.get('%s%s' % (self.live_server_url, '/'))
		self.assertEqual(
			self.selenium.find_elements_by_css_selector('.contact')[0].text,
			'Alejandro Romero'
		)

	def test_add_contact_linked(self):

		self.selenium.get('%s%s' % (self.live_server_url, '/'))
		self.assert_(
			self.selenium.find_element_by_link_text('add contact')
		)
	
	def test_add_contact(self):

		self.selenium.get('%s%s' % (self.live_server_url, '/'))
		self.selenium.find_element_by_link_text('add contact').click()

		self.selenium.find_element_by_id('id_first_name').send_keys('test')
		self.selenium.find_element_by_id('id_last_name').send_keys('contact')
		self.selenium.find_element_by_id('id_email').send_keys('test@test.co')
		self.selenium.find_element_by_id('id_confirm_email').send_keys('test@test.co')

		self.selenium.find_element_by_id('save_contact').click()

		self.assertEqual(self.selenium.find_elements_by_css_selector('.contact')[-1].text, 'test contact')

class EditContactFormTest(TestCase):
	
	def test_mismatch_email_is_invalid(self):

		form_data = flatten_to_dict(forms.ContactForm())

		form_data['first_name'] = 'Edwin'
		form_data['last_name'] = 'Chuky'
		form_data['email'] = 'chuky@chukyman.com'
		form_data['confirm_email'] = 'chuk@chukyman.com'

		bound_form = forms.ContactForm(data=form_data)
		self.assertFalse(bound_form.is_valid())

	def test_mismatch_email_is_invalid(self):

		form_data = flatten_to_dict(forms.ContactForm())

		form_data['first_name'] = 'Edwin'
		form_data['last_name'] = 'Chuky'
		form_data['email'] = 'chuky@chukyman.com'
		form_data['confirm_email'] = 'chuky@chukyman.com'

		bound_form = forms.ContactForm(data=form_data)
		self.assert_(bound_form.is_valid())