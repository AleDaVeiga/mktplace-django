from django.shortcuts import render, redirect, get_object_or_404

from portal.models import Product, Category
from portal.form import ProductForm


def home(request):
    return render(request, 'portal/home.html', {})


def my_ads(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'products': products
    }
    return render(request, 'portal/my_ads.html', context)


def product_new(request):
    context = {}
    categories = Category.objects.all()
    
    form = ProductForm()
    if request.method == 'POST':
        if form.is_valid():
            product = Product()
            product.name = form.cleaned_data['name']
            product.quantity = form.cleaned_data['quantity']
            product.price = form.cleaned_data['price']
            product.short_description = form.cleaned_data['short_description']
            product.description = form.cleaned_data['description']
            category = Category.objects.filter(pk=form.cleaned_data['category']).first()
            if category:
                product.categories = category

            product.save()
            return redirect('my_ads')
        context['form'] = form,
        return render(request, 'portal/product_new.html', context)
            
    context['form'] = form,
    context['categories'] = categories,

    return render(request, 'portal/product_new.html', context)


def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all()

    form = ProductForm()

    if request.method == 'POST':
        if form.is_valid():
            product = Product()
            product.name = form.cleaned_data['name']
            product.quantity = form.cleaned_data['quantity']
            product.price = form.cleaned_data['price']
            product.short_description = form.cleaned_data['short_description']
            product.description = form.cleaned_data['description']
            category = Category.objects.filter(pk=form.cleaned_data['category']).first()
            if category:
                product.categories = category

            product.save()
            form = ProductForm()

    context = {
        'form': form,
        'product': product,
        'categories': categories
    }

    return render(request, 'portal/product_edit.html', context)
