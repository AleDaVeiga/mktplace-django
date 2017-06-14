from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from billing.models import Order
from billing.forms import PaymentForm
from billing.services import BillingService

from portal.models import Product

import logging


@login_required
def payment(request, product_id):
    context = {}
    product = get_object_or_404(Product, pk=product_id)
    form = PaymentForm()
    context['product'] = product
    context['form'] = form

    user = request.user

    if request.method == 'POST' and request.POST.get("first_name", ""):
        form = PaymentForm(request.POST)
        if form.is_valid():
            full_name = request.POST.get('first_name').split(' ', 1)

            card_data = {
                'description': 'Market Place Payment',
                'item_type': 'credit_card',
                'data': {
                    'number': request.POST.get('number'),
                    'verification_value': request.POST.get('verification_value'),
                    'first_name': full_name[0],
                    'last_name': full_name[1],
                    'month': request.POST.get('month'),
                    'year': request.POST.get('year')
                }

            }

            context['form'] = form

            order = BillingService().charge(user, product, card_data)
            return redirect('billing_payment_order', order.id)
        return render(request, 'billing/payment.html', context)

    return render(request, 'billing/payment.html', context)


@login_required
def purchases(request):

    orders = Order.objects.filter(user=request.user)

    paginator = Paginator(orders, 15)
    page = request.GET.get('page', 1)

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {
        'orders': orders
    }

    return render(request, 'billing/purchases.html', context)


@login_required
def item_purchase(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if order.user != request.user:
        return redirect('home')

    context = {
        'order': order
    }

    return render(request, 'billing/item_purchase.html', context)


@login_required
def sales(request):

    orders = Order.objects.filter(merchant=request.user, status='Approved')

    paginator = Paginator(orders, 15)
    page = request.GET.get('page', 1)

    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {
        'orders': orders
    }

    return render(request, 'billing/sales.html', context)