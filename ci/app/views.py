# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import Context, RequestContext
from app.models import Item, Category, Picture
from app.forms import CategoryForm, ItemForm, DeleteCategory, DeleteItem
from django.http import StreamingHttpResponse
import json
from django.core.serializers import serialize

from django.contrib.auth.decorators import login_required

from app.serializers import CategorySerializer

from rest_framework import viewsets

from datetime import datetime

def index(request):
	context = {'title' : 'Hola CIDEI'}

	response = render_to_response('index.html', context, context_instance=RequestContext(request))
	# Get the number of visits to the site.
	# We use the COOKIES.get() function to obtain the visits cookie.
	# If the cookie exists, the value returned is casted to an integer.
	# If the cookie doesn't exist, we default to zero and cast that.
	visits = int(request.COOKIES.get('visits', '0'))
	# Does the cookie last_visit exist?
	if 'last_visit' in request.COOKIES:
		# Yes it does! Get the cookie's value.
		last_visit = request.COOKIES['last_visit']
		# Cast the value to a Python date/time object.
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
		# If it's been more than a day since the last visit...
		if (datetime.now() - last_visit_time).days == 0:
			# ...reassign the value of the cookie to +1 of what it was before...
			response.set_cookie('visits', visits+1)
			# ...and update the last visit cookie, too.
			response.set_cookie('last_visit', datetime.now())
	else:
		# Cookie last_visit doesn't exist, so create it to the current date/time.
		response.set_cookie('last_visit', datetime.now())
		response.set_cookie('visits', 0)
	#### NEW CODE ####
	if request.session.get('last_visit'):
		# The session has a value for the last visit
		last_visit_time = request.session.get('last_visit')
		visits = request.session.get('visits', 0)

		if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days == 0:
			request.session['visits'] = visits + 1
			request.session['last_visit'] = str(datetime.now())
		else:
			# The get returns None, and the session does not have a value for the last visit.
			request.session['last_visit'] = str(datetime.now())
			request.session['visits'] = 1
			#### END NEW CODE ####

		print request.session.get('sessionid')

	# Return response back to the user, updating any cookies that need changed
	return response

@login_required()
def categories(request):
	categories = Category.objects.all()
	context = Context({'title' : 'Hola CIDEI', 'categories' : categories})
	return render_to_response('categories.html', context, context_instance=RequestContext(request))

@login_required()
def category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	context = Context({'title' : 'Detalle categoria', 'category' : category})
	return render_to_response('category-details.html', context, context_instance=RequestContext(request))

@login_required()
def add_category(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			# Crear un nuevo category
			category = Category.objects.create(
				name = form.cleaned_data['name'],
				slug = form.cleaned_data['slug'],
			)
			# Siempre que cree el dato correctamente redireccionar
			return HttpResponseRedirect('/categories/%s/' % category.slug)
	else:
		form = CategoryForm()

	context = Context({'title':'Creación de categorias', 'form': form})
	return render_to_response('add-category.html', context, context_instance=RequestContext(request))

@login_required()
def edit_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			category.name = form.cleaned_data['name']
			category.slug = form.cleaned_data['slug']
			category.save()
			# Siempre que cree el dato correctamente redireccionar
			return HttpResponseRedirect('/categories/%s/' % category.slug)
	else:
		category_data = {
			'name' : category.name,
			'slug' : category.slug
		}
		form = CategoryForm(initial=category_data)
	context = Context({'title' : 'Editar la categoria', 'form' : form})
	return render_to_response('add-category.html', context, context_instance=RequestContext(request))

@login_required()
def delete_category(request, slug):
	item = get_object_or_404(Category, slug=slug)
	if request.method == "POST":
		form = DeleteCategory(request.POST)
		if form.is_valid():
			item.delete()
			return HttpResponseRedirect('/categories/')
	else:
		form = DeleteCategory()
		context = Context({'title' : 'Borrar categoria', 'form' : form})
		return render_to_response('add-category.html', context, context_instance=RequestContext(request))

@login_required()
def items(request):
	items = Item.objects.all()
	context = Context({'title' : 'Hola CIDEI', 'items' : items})
	return render_to_response('items.html', context)

@login_required()
def item(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	pictures = Picture.objects.filter(item=item)
	count_pictures = pictures.count()
	context = Context({
		'title' : 'Hola CIDEI',
		'item' : item,
		'pictures':pictures,
		'count_pictures' : count_pictures
	})
	return render_to_response('item-details.html', context, context_instance=RequestContext(request))

@login_required()
def add_item(request):
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			# Crear un nuevo item
			item = Item.objects.create(
				listing = form.cleaned_data['listing'],
				name = form.cleaned_data['name'],
				category=form.cleaned_data['category'],
				department=form.cleaned_data['department'],
				description = form.cleaned_data['description'],
				update_item = form.cleaned_data['update_item'],
			)
			# Siempre que cree el dato correctamente redireccionar
			return HttpResponseRedirect('/items/%s/' % item.id)
	else:
		form = ItemForm()

	context = Context({'title' : 'Adicionar item', 'form' : form})
	return render_to_response('add-item.html', context, context_instance=RequestContext(request))

@login_required()
def edit_item(request, item_id):
	item = get_object_or_404(Item, pk=item_id)
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			item.listing = form.cleaned_data['listing']
			item.name = form.cleaned_data['name']
			item.category = form.cleaned_data['category']
			item.department = form.cleaned_data['department']
			item.description = form.cleaned_data['description']
			item.update_item = form.cleaned_data['update_item']
			item.save()
			# Siempre que cree el dato correctamente redireccionar
			return HttpResponseRedirect('/items/%s/' % item.id)
	else:
		item_data = {
			'listing' : item.listing,
			'name' : item.name,
			'category' : item.category.id,
			'department' : item.department,
			'description' : item.description,
			'update_item' :item.update_item
		}
		form = ItemForm(initial=item_data)
	context = Context({'title' : 'Editar el item', 'form' : form})
	return render_to_response('add-item.html', context, context_instance=RequestContext(request))

@login_required()
def ajax_items(request):
	if request.is_ajax():
		items = Item.objects.all()
		print items
		items = serialize('json', items)
		print items
		items = json.dumps(items)
		print items
		return StreamingHttpResponse(items, content_type='application/json')
	else:
		return StreamingHttpResponse(json.dumps({'test': 'error'}), content_type='application/json')

def ajax_item(request, item_id):
	if request.is_ajax():
		item = Item.objects.filter(id=item_id)
		print item
		item = serialize('json', item)
		print item
		item = json.dumps(item)
		print item
		return StreamingHttpResponse(item, content_type='application/json')
	else:
		return StreamingHttpResponse(json.dumps({'test': 'error'}), content_type='application/json')

@login_required()
def delete_item(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	if request.method == "POST":
		form = DeleteItem(request.POST)
		if form.is_valid():
			item.delete()
			return HttpResponseRedirect('/items/')
	else:
		form = DeleteItem()
		context = Context({'title' : 'Borrar item', 'form' : form})
		return render_to_response('add-item.html', context, context_instance=RequestContext(request))

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer