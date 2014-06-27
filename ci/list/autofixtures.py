from list.models import Category, Item
from autofixture import generators, register, AutoFixture
import random

nouns = ("Hardware", "Sofware", "Test-Software", "Test-Hardware", "App", "BigData",)

class CategoryFixture(AutoFixture):
	field_values = {
		'name' : generators.random.choice(nouns),
		'slug' : generators.SlugGenerator('cidei'),
	}

register(Category, CategoryFixture)