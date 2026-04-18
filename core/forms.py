from django import forms
from .models import Producto, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@empresa.com'):
            raise forms.ValidationError("El email debe tener el dominio corporativo @empresa.com.")
        return email