from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from contacts.models import Contact

class ContactView(DetailView):
	model = Contact
	template_name = 'contacts/detail_contact.html'

class DeleteContactView(DeleteView):
	model = Contact
	template_name = 'contacts/delete_contact.html'

	def get_success_url(self):
		return reverse('contact-list')

class UpdateContactView(UpdateView):
	model = Contact
	template_name = 'contacts/edit_contact.html'

	def get_success_url(self):
		return reverse('contact-list')

	def get_context_data(self, **kwargs):
		context = super(UpdateContactView, self).get_context_data(**kwargs)
		context['action'] = reverse('contact-edit', kwargs={'pk' : self.get_object().id})

		return context

class CreateContactView(CreateView):
	model = Contact

	template_name = 'contacts/edit_contact.html'

	def get_success_url(self):
		return reverse('contact-list')

	def get_context_data(self, **kwargs):
		context = super(CreateContactView, self).get_context_data(**kwargs)
		context['action'] = reverse('contact-new')

		return context

class ListContactView(ListView):
	model = Contact
	template_name = 'contacts/contact_list.html'

def hello_world(request):
	return HttpResponse("hello!")

class MyView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("hello")