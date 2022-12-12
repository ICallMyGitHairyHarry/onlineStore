from django.shortcuts import render, get_object_or_404
from django.views import generic

from catalogue.models import Product


def index(request):
    products_list = Product.objects.all()
    items = {}
    for i in request.session.keys():
        try:
            items[int(i)] = request.session[i]
        except ValueError:
            continue
    context = {
        'products_list': products_list,
        'session_items': items
    }
    return render(request, 'catalogue/index.html', context)


def product(request, product_id):
    product_amount = None
    product_item = get_object_or_404(Product, pk=product_id)
    if str(product_id) in request.session.keys():
        product_amount = request.session[str(product_id)]
    context = {
        'product': product_item,
        'product_amount': product_amount
    }
    return render(request, 'catalogue/product.html', context)
