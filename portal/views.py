from django.shortcuts import render, get_object_or_404

from portal.models import Product


def home(request):
    return render(request, 'portal/home.html', {})


def my_ads(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'products': products
    }
    return render(request, 'portal/my_ads.html', context)


def product_edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'portal/product_edit.html', context)
