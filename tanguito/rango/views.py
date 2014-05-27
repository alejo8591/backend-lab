from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

# Create your views here.

def index(request):

	context = RequestContext(request)

	context_dict = {'boldmessage' : "I am a bold context"}

	return render_to_response('index.html', context_dict, context)