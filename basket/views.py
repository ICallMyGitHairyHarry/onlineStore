import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from basket.models import Order
from catalogue.models import Product
from registration.models import Adm, Customer


def basket(request):
    product_list = []
    items = {}
    prices = {}
    for i in request.session.keys():
        try:
            items[int(i)] = request.session[i]
        except ValueError:
            continue
    for key in items.keys():
        product_list.append(Product.objects.get(pk=str(key)))
    for product in product_list:
        prices[product.id] = product.pr_price * items[product.id]
    context = {
        'product_list': product_list,
        'product_items': items,
        'product_prices': prices
    }
    return render(request, 'basket/basket.html', context)


def add_product(request, product_id):
    if product_id in request.session:
        request.session[product_id] += 1
    else:
        request.session[product_id] = 1
    # print(request.session.items())
    return HttpResponse()


def subtract_product(request, product_id):
    request.session[product_id] -= 1
    if request.session[product_id] == 0:
        del request.session[product_id]
    # print(request.session.items())
    return HttpResponse()


def order(request):
    return render(request, 'basket/order.html', )


def create_order(request):
    products = {}
    full_price = 0
    user_order = None

    for i in request.session.keys():
        try:
            products[int(i)] = request.session[i]
        except ValueError:
            continue

    if products == {}:
        return HttpResponse("Добавьте товары и оформите заказ")

    for product in products:
        full_price += Product.objects.get(pk=product).pr_price * products[product]

    current_seller = Adm.objects.get(pk=1)
    if request.user.is_authenticated:
        current_user = request.user.customer
        user_order = Order(cr_date=datetime.datetime.now(), full_pr=full_price, customer=current_user,
                           seller=current_seller)
    else:
        temp_login = 'temp' + str(datetime.datetime.now().timestamp())
        user_data = [request.POST['login'], request.POST['last_name'], request.POST['first_name']]
        customer_data = [request.POST['phone'], request.POST['district'], request.POST['street'], request.POST['house'],
                         request.POST['corp'], request.POST['flat'], request.POST['p_index']]

        temp_user = User.objects.create_user(username=temp_login, password=temp_login,
                                             email=user_data[0], first_name=user_data[2], last_name=user_data[1])
        temp_user.save()
        temp_customer = Customer(temp_user.id, temp_user.id, customer_data[0], customer_data[1], customer_data[2],
                                 customer_data[3], customer_data[4], customer_data[5], customer_data[6])
        temp_customer.save()
        user_order = Order(cr_date=datetime.datetime.now(), full_pr=full_price, customer=temp_customer,
                           seller=current_seller)

    user_order.save()

    for product in products:
        prod_list = user_order.prod_list_set.create(product_id=product, pr_amount=products[product])
        prod_list.save()
        del request.session[str(product)]

    new_order = Order.objects.get(pk=user_order.id)
    context = {
        'order': new_order
    }

    return render(request, 'basket/order_success.html', context)
