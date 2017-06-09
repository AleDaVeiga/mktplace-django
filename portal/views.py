from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from portal.models import Product, Category, ProductQuestion, UserProfile, ProductAnswer
from portal.forms import ProductForm, ProductFormEdit, ProductQuestionForm, UserProfileForm, UserForm, AnswerQuestionForm, PaymentForm

import algoliasearch_django as algoliasearch

import logging


def home(request):
    categories = Category.objects.filter(hidden=False, parent__isnull=True).order_by('name')
    products = Product.objects.filter(status='Active')

    paginator = Paginator(products, 20)
    page = request.GET.get('page', 1)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'products': products
    }

    return render(request, 'portal/home.html', context)


@login_required
def my_ads(request):
    products = Product.objects.filter(user=request.user)

    paginator = Paginator(products, 15)
    page = request.GET.get('page', 1)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products
    }
    return render(request, 'portal/my_ads.html', context)


def product_show(request, slug):
    product = get_object_or_404(Product, slug=slug, status='Active')
    questions = ProductQuestion.objects.filter(product=product, status='Active')
    form = ProductQuestionForm()

    context = {
        'form': form,
        'product': product,
        'questions': questions
    }
    return render(request, 'portal/product_show.html', context)


def product_new_question(request, product_id):
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


@login_required
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


@login_required
def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all()
    form = ProductFormEdit(instance=product)

    if request.method == 'POST':
        form = ProductFormEdit(request.POST)
        if form.is_valid():
            product.user = request.user
            product.name = form.cleaned_data['name']
            product.quantity = form.cleaned_data['quantity']
            product.price = form.cleaned_data['price']
            product.short_description = form.cleaned_data['short_description']
            product.description = form.cleaned_data['description']
            product.status = form.cleaned_data['status']
            product.categories = form.cleaned_data['categories']
            product.save()
            return redirect('my_ads')

    context = {
        'form': form,
        'product': product,
        'categories': categories
    }

    return render(request, 'portal/product_edit.html', context)


# dados do user
@login_required
def my_data(request):
    user = User.objects.get(pk=request.user.pk)
    user_form = UserForm(instance=user)

    try:
        user_profile = UserProfile.objects.get(user=user)
        profile_form = UserProfileForm(instance=user_profile)
    except:
        profile_form = UserProfileForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.save()

            try:
                user_profile = user_profile
            except:
                user_profile = UserProfile()
                user_profile.user = user
            user_profile.cpf = profile_form.cleaned_data['cpf']
            user_profile.address = profile_form.cleaned_data['address']
            user_profile.number = profile_form.cleaned_data['number']
            user_profile.address2 = profile_form.cleaned_data['address2']
            user_profile.city = profile_form.cleaned_data['city']
            user_profile.district = profile_form.cleaned_data['district']
            user_profile.state = profile_form.cleaned_data['state']
            user_profile.country = profile_form.cleaned_data['country']
            user_profile.zipcode = profile_form.cleaned_data['zipcode']
            user_profile.phone = profile_form.cleaned_data['phone']
            user_profile.save()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user
    }

    return render(request, 'portal/my_data.html', context)


# questions
def product_question(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'portal/product_question.html', context)


def product_answer_question(request, product_id, question_id):
    product = get_object_or_404(Product, pk=product_id)
    question = get_object_or_404(ProductQuestion, pk=question_id)

    form = AnswerQuestionForm()

    context = {
        'form': form,
        'product': product,
        'question': question,
    }

    return render(request, 'portal/product_answer_question.html', context)


def answer_question_new(request, product_id, question_id):
    product = get_object_or_404(Product, pk=product_id)
    question = get_object_or_404(ProductQuestion, pk=question_id)

    if request.method == 'POST':
        form = AnswerQuestionForm(request.POST)
        if form.is_valid():
            product_answer = ProductAnswer()
            product_answer.user = request.user
            product_answer.answer = form.cleaned_data['answer']
            product_answer.product_question = question
            product_answer.save()

            return redirect('product_question', product.id)
    return redirect('home')


def product_list_questions(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    questions = ProductQuestion.objects.filter(product=product).order_by('-id')

    paginator = Paginator(questions, 15)
    page = request.GET.get('page', 1)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    context = {
        'product': product,
        'questions': questions,
    }
    return render(request, 'portal/product_list_questions.html', context)


def product_answer_question_edit(request, product_id, question_id, answer_id):
    product = get_object_or_404(Product, pk=product_id)
    question = get_object_or_404(ProductQuestion, pk=question_id)
    answer = ProductAnswer.objects.get(pk=answer_id)

    form = AnswerQuestionForm(instance=answer)

    if request.method == 'POST':
        form = AnswerQuestionForm(request.POST)
        if form.is_valid():
            answer.user = request.user
            answer.answer = form.cleaned_data['answer']
            answer.product_question = question
            answer.save()

            return redirect('product_list_questions', product.id)

    context = {
        'form': form,
        'product': product,
        'question': question,
    }

    return render(request, 'portal/product_answer_question_edit.html', context)


# busca
def search(request):
    categories = Category.objects.filter(hidden=False, parent__isnull=True).order_by('name')
    qs = request.GET.get('qs', "")
    str_category = request.GET.get('category', "")
    page = request.GET.get('page', "0")

    results = None
    cat_name = ""
    next_page = ""
    previous_page = ""

    if page:
        next_page = int(page) + 1
        previous_page = int(page) - 1

    if qs:
        params = {"hitsPerPage": 1, "page": page, }
        results = algoliasearch.raw_search(Product, qs, params)

    if str_category:
        cat = get_object_or_404(Category, slug=str_category)
        cat_name = cat.name
        results = Product.objects.filter(categories=cat)

        paginator = Paginator(results, 1)
        page = request.GET.get('page', 1)

        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)


    logging.warning(results)

    context = {
        'str_category': str_category,
        'cat_name': cat_name,
        'categories': categories,
        'results': results,
        'qs': qs,
        'next_page': next_page,
        'previous_page': previous_page,
    }

    return render(request, 'portal/product_search.html', context)


def payment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = PaymentForm()

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'portal/payment.html', context)
