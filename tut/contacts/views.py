from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView
from contacts.models import Contact

class ListContactView(ListView):
	model = Contact
	template_name = 'contacts/contact_list.html'

def hello_world(request):
	return HttpResponse("hello!")

class MyView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("hello")