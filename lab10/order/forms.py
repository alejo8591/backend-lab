from django import forms
from order.models import Customer, Product, Stock, Order

class CustomerForm(forms.ModelForm):

    customer_name = forms.CharField(max_length=128,
                                    help_text='Ingrese el Nombre Completo.',
                                    widget=forms.TextInput(attrs={'class':'u-full-width'}))

    customer_address = forms.CharField(max_length=64,
                                    help_text='Ingrese la Direccion Completa.',
                                    widget=forms.TextInput(attrs={'class':'u-full-width'}))

    customer_phone = forms.CharField(max_length=24,
                                    help_text='Ingrese el Teléfono.',
                                    widget=forms.TextInput(attrs={'class':'u-full-width'}))

    class Meta:
        model = Customer
        excludes = ('date_created_customer', 'date_updated_customer',)
        fields = ('customer_name', 'customer_address', 'customer_phone',)


class ProductForm(forms.ModelForm):

    product_name = forms.CharField(max_length=128,
                                    help_text='Indique Nombre del Producto.',
                                    widget=forms.TextInput(attrs={'class':'u-full-width'}))

    product_price = forms.DecimalField(max_digits=64,
                                    decimal_places = 2,
                                    help_text='Precio del Producto.', initial=0,
                                    widget=forms.TextInput(attrs={'class':'u-full-width'}))

    product_type = forms.CharField(max_length=128,
                                    help_text='Indique el Tipo de Producto.',
                                    widget=forms.TextInput(attrs={'class':'u-full-width'}))

    product_description = forms.CharField(widget=forms.Textarea(attrs={'class':'u-full-width'}),
                                    help_text='Indique el Tipo de Producto.')

    class Meta:
        model = Product
        excludes = ('date_created_product', 'date_updated_product',)
        fields = ('product_name', 'product_price', 'product_type', 'product_description',)


class StockForm(forms.ModelForm):

    stock_quantity = forms.IntegerField(help_text='Cantidad del Producto.', initial=0,
                                        widget=forms.TextInput(attrs={'class':'u-full-width'}))

    class Meta:
        model = Stock
        exclude = ('stock_product_id','date_created_stock',  'date_updated_stock',)
        fields = ('stock_quantity',)


class OrderForm(forms.ModelForm):

    order_customer_id = forms.ModelChoiceField(queryset=Customer.objects.all(),
                                    help_text='Seleccione el Nombre del Cliente.')

    order_product_id = forms.ModelChoiceField(queryset=Product.objects.all(),
                                    help_text='Seleccione el Producto(s).')

    order_amount = forms.DecimalField(help_text='Cantidad del Producto.', initial=0)

    class Meta:
        model = Order
        exclude = ('order_date', 'date_updated_customer',)
        fields = ( 'order_product_id','order_customer_id', 'order_amount',)
