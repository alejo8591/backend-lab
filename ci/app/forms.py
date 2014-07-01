from django import forms

from app.models import L_TYPES, Category, Item

class DeleteItem(forms.Form):
	delete = forms.BooleanField(label='Seleccione para Elimiar')

class DeleteCategory(forms.Form): 
	delete = forms.BooleanField(label='Seleccione para Elimiar')

class CategoryForm(forms.Form):
	name = forms.CharField(max_length=255)
	slug = forms.SlugField(max_length=255)

class ItemForm(forms.Form):
	listing = forms.ChoiceField(choices=L_TYPES, initial='t')
	name = forms.CharField(max_length=255)
	category = forms.ModelChoiceField(Category.objects.all())
	department = forms.CharField(max_length=255)
	description = forms.CharField(widget=forms.Textarea)
	update_item = forms.DateTimeField()

	def clean_department(self):
		data = self.cleaned_data['department']

		if data not in ['Develop', 'Tools', 'Electronics']:
			raise forms.ValidationError('El departamente no existe en la empresa')
		return data