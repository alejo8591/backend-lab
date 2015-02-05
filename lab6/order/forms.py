from django import forms
from order.models import Customer, Product, Stock, Order

class CustomerForm(forms.ModelForm):

    customer_name = forms.CharField(max_length=128,
                                    help_text='Ingrese el Nombre Completo.')

    customer_address = forms.CharField(max_length=64,
                                    help_text='Ingrese la Direccion Completa.')

    customer_phone = forms.CharField(max_length=24,
                                    help_text='Ingrese el Teléfono.')

    class Meta:
        model = Customer
        fields = ('customer_name', 'customer_address', 'customer_phone',)


class ProductForm(forms.ModelForm):

    product_name = forms.CharField(max_length=128,
                                    help_text='Indique Nombre del Producto.')

    product_price = forms.DecimalField(max_digits=64,
                                    decimal_places = 2,
                                    help_text='Precio del Producto.', initial=0)

    product_type = forms.CharField(max_length=128,
                                    help_text='Indique el Tipo de Producto.')

    product_description = forms.CharField(widget=forms.Textarea,
                                    help_text='Indique el Tipo de Producto.')

    class Meta:
        model = Product
        fields = ('product_name', 'product_price', 'product_type', 'product_description',)


class StockForm(forms.ModelForm):

    stock_quantity = forms.IntegerField(help_text='Cantidad del Producto.', initial=0)

    class Meta:
        model = Stock
        exclude = ('stock_product_id',)
        fields = ('stock_quantity',)

class OrderForm(forms.ModelForm):

    order_customer_id = forms.ModelChoiceField(queryset=Customer.objects.all(),
                                    help_text='Seleccione el Nombre del Cliente.')

    order_product_id = forms.ModelChoiceField(queryset=Product.objects.all(),
                                    help_text='Seleccione el Producto(s).')

    order_amount = forms.DecimalField(help_text='Cantidad del Producto.', initial=0)

    class Meta:
        model = Order
        exclude = ('order_date',)
        fields = ( 'order_product_id','order_customer_id', 'order_amount',)
