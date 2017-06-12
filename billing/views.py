from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from billing.forms import PaymentForm
from billing.services import BillingService

from portal.models import Product

import logging


@login_required
def payment(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    form = PaymentForm()

    user = request.user

    if request.method == 'POST':
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

            charge = BillingService().charge(user, product, card_data)

            logging.warning(charge)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'billing/payment.html', context)
