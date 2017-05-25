from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(label='Nome',
                           max_length=255,
                           required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'})
                           )

    quantity = forms.CharField(label='Quantidade',
                               max_length=10,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'})
                               )

    price = forms.CharField(label='Valor',
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'})
                            )

    short_description = forms.CharField(label='Breve Descrição',
                                        required=True,
                                        widget=forms.TextInput(attrs={'class': 'form-control'})
                                        )

    description = forms.CharField(label='Descrição',
                                  widget=forms.Textarea(attrs={'class': 'form-control'})
                                  )
