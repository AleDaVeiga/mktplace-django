from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from billing.forms import PaymentForm

from portal.models import Product


@login_required
def payment(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    form = PaymentForm()

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'billing/payment.html', context)
