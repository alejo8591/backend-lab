from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View, ListView, CreateView
from contacts.models import Contact

class CreateContactView(CreateView):
	model = Contact

	template_name = 'contacts/edit_contact.html'

	def get_success_url(self):
		return reverse('contact-list')

class ListContactView(ListView):
	model = Contact
	template_name = 'contacts/contact_list.html'

def hello_world(request):
	return HttpResponse("hello!")

class MyView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("hello")