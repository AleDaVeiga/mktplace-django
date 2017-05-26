from django.shortcuts import render, redirect, get_object_or_404

from portal.models import Product, Category, ProductQuestion
from portal.forms import ProductForm, ProductQuestionForm

import logging


def home(request):
    return render(request, 'portal/home.html', {})


def my_ads(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'products': products
    }
    return render(request, 'portal/my_ads.html', context)


def product_show(request, slug):
    product = get_object_or_404(Product, slug=slug, status='Active')
    questions = ProductQuestion.objects.filter(product=product, status='Active')

    logging.warning(questions)

    context = {
        'product': product,
        'questions': questions
    }
    return render(request, 'portal/product_show.html', context)


def product_question(request, product_id):
    product = get_object_or_404(Product, id=product_id, status='Active')

    if request.method == 'POST':
        form = ProductQuestionForm(request.POST)
        if form.is_valid():
            question = ProductQuestion()
            question.user = request.user
            question.product = product
            question.question = form.cleaned_data['question']
            question.status = 'Active'
            question.save()

    return redirect('product_show', product.slug)


def product_new(request):
    categories = Category.objects.all()
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product()
            product.user = request.user
            product.name = form.cleaned_data['name']
            product.quantity = form.cleaned_data['quantity']
            product.price = form.cleaned_data['price']
            product.short_description = form.cleaned_data['short_description']
            product.description = form.cleaned_data['description']
            product.status = form.cleaned_data['status']
            product.save()
            
            categories = Category.objects.filter(id__in=request.POST.getlist('categories'))
            if categories:
                for category in categories:
                    product.categories.add(category)
                
            return redirect('my_ads')
    
    context = {
        'form': form,
        'categories': categories
    }

    return render(request, 'portal/product_new.html', context)


def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = product
            product.user = request.user
            product.name = form.cleaned_data['name']
            product.quantity = form.cleaned_data['quantity']
            product.price = form.cleaned_data['price']
            product.short_description = form.cleaned_data['short_description']
            product.description = form.cleaned_data['description']
            product.status = form.cleaned_data['status']
            categories = Category.objects.filter(id__in=request.POST.getlist('categories'))
            if categories:
                product.categories = categories
    
            product.save()
            return redirect('my_ads')

    context = {
        'form': form,
        'product': product,
        'categories': categories
    }

    return render(request, 'portal/product_edit.html', context)
