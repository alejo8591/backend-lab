from bookmsrk.models import Category, Page
from autofixture import generators, register, AutoFixture

import random

nouns = ("Hardware", "Software", "Test-Software", "Test-Hardware", "Apps", "BigData",)

class CategoryAutoFixture(AutoFixture):
	field_values = {
		'name' : generators.StaticGenerator(random.choice(nouns)),
	}
"""
class PageFixture(AutoFixture):
	field_values = {
		'listing' : generators.random.choice(lista),
#		'name' : ,
#		'category' : ,
#		'department' : ,
#		'description' : ,
#		'posted_on' : ,
		'update_item' : generators.DateTimeGenerator(),
	}
"""
register(Category, CategoryFixture)
#register(Item, ItemFixture)
