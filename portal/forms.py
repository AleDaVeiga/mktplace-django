from django import forms
from portal.models import Category, Product


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
                               widget=forms.Textarea(),
                               required=True,
                               )
