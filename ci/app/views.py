# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import Context, RequestContext
from app.models import Item, Category, Picture
from app.forms import CategoryForm, ItemForm
from django.http import HttpResponse
import json
from django.core.serializers import serialize

def index(request):
	context = Context({'title' : 'Hola CIDEI'})
	return render_to_response('index.html', context)

def categories(request):
	categories = Category.objects.all()
	context = Context({'title' : 'Hola CIDEI', 'categories' : categories})
	return render_to_response('categories.html', context)

def category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	context = Context({'title' : 'Detalle categoria', 'category' : category})
	return render_to_response('category-details.html', context)

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

def items(request):
	items = Item.objects.all()
	context = Context({'title' : 'Hola CIDEI', 'items' : items})
	return render_to_response('items.html', context)

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
	return render_to_response('item-details.html', context)

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

def ajax_items(request):
	if request.is_ajax():
		items = Item.objects.all()
		print items
		items = serialize('json', items)
		print items
		items = json.dumps(items)
		print items
		return HttpResponse(items, content_type='application/json')
	else:
		return HttpResponse(json.dumps({'test': 'error'}), content_type='application/json')

def ajax_item(request, item_id):
	if request.is_ajax():
		item = Item.objects.filter(id=item_id)
		print item
		item = serialize('json', item)
		print item
		item = json.dumps(item)
		print item
		return HttpResponse(item, content_type='application/json')
	else:
		return HttpResponse(json.dumps({'test': 'error'}), content_type='application/json')

