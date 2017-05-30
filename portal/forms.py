from django import forms
from portal.models import Category, Product, UserProfile


class ProductFormEdit(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )

        widgets = {
            'account_type': forms.Select(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'account_type': "Tipo de Conta",
            'company_name': "Nome da Empresa",
            'cpf_cnpj': "CPF/CNPJ",
            'address': "Endereço",
            'address2': "Complemento",
            'city': "Cidade",
            'district': "Bairro",
            'state': "Estado",
            'country': "País",
            'zipcode': "CEP",
            'phone': "Telefone",
        }


# exemplo com forms.ModelForm usado no edit
class ProductFormEdit(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('slug', 'user', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': "Nome",
            'categories': "Categories",
            'quantity': "Quantidade",
            'price': "Preço",
            'short_description': "Descrição curta",
            'description': "Descrição",
        }



# exemplo com forms.Form usado no new
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
                                  required=True,
                                  widget=forms.Textarea(attrs={'class': 'form-control'})
                                  )

    choices = [(cat.id, str(cat)) for cat in Category.objects.all()]
    categories = forms.MultipleChoiceField(label='Categorias',
                                           required=True,
                                           widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
                                           choices=choices,
                                           )

    STATUS_CHOICES = (
        ('Active', 'Ativo',),
        ('Inactive', 'Inativo',),
    )

    status = forms.ChoiceField(label='Status',
                               widget=forms.Select(attrs={'class': 'form-control'}),
                               required=True,
                               choices=STATUS_CHOICES,
                               )


class ProductQuestionForm(forms.Form):
    question = forms.CharField(label='Perguntar',
                               widget=forms.Textarea(attrs={'class': 'form-control',
                                                            'id': 'question',
                                                            'placeholder': 'Escreva uma pergunta...'
                                                            }),
                               required=True,
                               )
