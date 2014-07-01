from app.models import Category, Item
from autofixture import generators, register, AutoFixture

import random

nouns = ("Hardware", "Software", "Test-Software", "Test-Hardware", "Apps", "BigData",)

class CategoryFixture(AutoFixture):
	field_values = {
		'name' : generators.random.choice(nouns),
		'slug' : generators.SlugGenerator('cidei'),
	}

class ItemFixture(AutoFixture):
	field_values = {
		'listing' : generators.random.choice(lista),
#		'name' : ,
#		'category' : ,
#		'department' : ,
#		'description' : ,
#		'posted_on' : ,
		'update_item' : generators.DateTimeGenerator(),
	}	
		
register(Category, CategoryFixture)
register(Item, ItemFixture)