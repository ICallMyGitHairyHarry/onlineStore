import datetime

from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from basket.models import Order, Prod_list
from catalogue.models import Product
from userProfile.forms import ProductForm


def user_profile(request):
    # если пользователь авторизован
    if request.user.is_authenticated:

        # если авторизован продавец, владелец или системный администратор
        if hasattr(request.user, 'adm'):

            # если авторизован продавец
            if request.user.adm.u_role == '1':
                return render(request, 'userProfile/profile_seller.html', {'date': datetime.date.today()})

            # если авторизован владелец
            elif request.user.adm.u_role == '2':

                # расчет прибыли
                if 'first_date_profit' in request.POST:
                    start_date_profit = request.POST['first_date_profit']
                    end_date_profit = request.POST['last_date_profit']
                    paid_orders = Order.objects.filter(pay_date__range=(start_date_profit, end_date_profit),
                                                       ord_status='2')
                else:
                    paid_orders = Order.objects.filter(ord_status='2')

                profit = 0
                costs = 0
                for paid_order in paid_orders:
                    for prod in paid_order.prod_list_set.all():
                        costs += prod.product.pr_cost * prod.pr_amount
                    profit += paid_order.full_pr
                profit -= costs

                # расчет рейтинга
                products_rating = {}
                for product in Product.objects.all():
                    if 'first_date_rating' in request.POST:
                        start_date_rating = request.POST['first_date_rating']
                        end_date_rating = request.POST['last_date_rating']
                        total_pr_amount = Prod_list.objects.filter(
                            order__ord_status='2',
                            product_id=product.id,
                            order__pay_date__range=(start_date_rating, end_date_rating))
                    else:
                        total_pr_amount = Prod_list.objects.filter(order__ord_status='2', product_id=product.id)

                    if total_pr_amount.count() != 0:
                        total_pr_amount = total_pr_amount.aggregate(total=Sum('pr_amount'))['total']
                        product_profit = (product.pr_price - product.pr_cost) * total_pr_amount
                        products_rating[product.id] = product_profit

                products_rating = sorted(products_rating.items(), key=lambda x: x[1], reverse=True)
                products_rating = dict(products_rating[0:3])

                top_products = []
                for pr in products_rating:
                    top_products.append(Product.objects.get(pk=pr))

                context = {
                    'date': datetime.date.today(),
                    'profit': profit,
                    'products_rating': products_rating,
                    'top_products': top_products,
                }
                if 'first_date_profit' in request.POST:
                    context['start_date_profit'] = request.POST['first_date_profit']
                    context['end_date_profit'] = request.POST['last_date_profit']
                elif 'first_date_rating' in request.POST:
                    context['start_date_rating'] = request.POST['first_date_rating']
                    context['end_date_rating'] = request.POST['last_date_rating']

                return render(request, 'userProfile/profile_owner.html', context)

            # если авторизован системный администратор
            else:
                return render(request, 'userProfile/profile_admin.html', {'date': datetime.date.today()})

        # если авторизован покупатель
        orders = None
        overall_cost = 0
        search_failed = False

        if 'first_date' in request.POST:
            start_date = request.POST['first_date']
            end_date = request.POST['last_date']
            orders = Order.objects.filter(cr_date__range=(start_date, end_date), customer_id=request.user.customer.id)
            if orders.count() == 0:
                search_failed = True
        else:
            orders = Order.objects.filter(customer_id=request.user.customer.id)

        for order in orders:
            overall_cost += order.full_pr

        context = {
            'orders': orders,
            'date': datetime.date.today(),
            'overall_cost': overall_cost,
            'search_failed': search_failed,
        }

        if 'first_date' in request.POST:
            context['start_date'] = request.POST['first_date']
            context['end_date'] = request.POST['last_date']

        return render(request, 'userProfile/profile_customer.html', context)

    else:

        return render(request, 'userProfile/profile_denied.html')


def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('userProfile:product_created'))
    else:
        form = ProductForm()

    return render(request, 'userProfile/new_product.html', {'form': form})


def product_created(request):
    last_product = Product.objects.last()

    context = {
        'new_product': last_product,
    }

    return render(request, 'userProfile/product_created.html', context)


def change_product(request):
    products_list = Product.objects.all()

    context = {
        'products_list': products_list,
    }

    return render(request, 'userProfile/change_product.html', context)


def del_product(request, product_id):
    Product.objects.get(pk=product_id).delete()
    return HttpResponseRedirect(reverse('userProfile:change_product'))


def modify_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect('userProfile:product_modified', product.id)
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product
    }

    return render(request, 'userProfile/modify_product.html', context)


def product_modified(request, product_id):
    modified_product = Product.objects.get(pk=product_id)

    context = {
        'product': modified_product,
    }

    return render(request, 'userProfile/product_modified.html', context)


def change_status(request):
    unpaid_orders = Order.objects.filter(seller_id=request.user.adm.id, ord_status='1')
    paid_orders = Order.objects.filter(seller_id=request.user.adm.id, ord_status='2')

    context = {
        'unpaid_orders': unpaid_orders,
        # 'paid_orders': paid_orders,
    }

    return render(request, 'userProfile/change_status.html', context)


def change_order_status_paid(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.ord_status = '2'
    order.pay_date = datetime.datetime.now()
    order.save()

    return HttpResponseRedirect(reverse('userProfile:change_status'))


def change_order_status_unpaid(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.ord_status = '1'
    order.pay_date = None
    order.save()

    return HttpResponseRedirect(reverse('userProfile:change_status'))
