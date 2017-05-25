from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=255, required=True)
    quantity = forms.CharField(label='Quantidade', max_length=10, required=True)
    price = forms.CharField(label='Valor', required=True)
    short_description = forms.CharField(label='Breve Descrição', required=True)
    description = forms.CharField(label='Descrição', widget=forms.Textarea)
