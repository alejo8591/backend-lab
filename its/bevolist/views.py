from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from bevolist.models import *

def index(request):
	items = Item.objects.all()
	context = Context({'title' : 'Bevolist Site', 'items' : items})
	return render_to_response('bevolist/index.html', context)

def details(request, item_id):
	item = get_object_or_404(Item, id=item_id)

	context = Context({
		'title' : '%s Details' %item.name,
		'item' : item
	})
	return render_to_response('bevolist/details.html', context)