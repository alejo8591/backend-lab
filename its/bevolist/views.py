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

def category(request):
	categories = Category.objects.all()
	context = Context({'title' : 'Categories List', 'categories' :categories})

	return render_to_response('bevolist/categories.html', context)

def category_details(request, slug):
	category = get_object_or_404(Category, slug=slug)

	context = Context({
		'title' : 'Category: %s' %category.name,
		'category' : category
	})

	return render_to_response('bevolist/category.html', context)