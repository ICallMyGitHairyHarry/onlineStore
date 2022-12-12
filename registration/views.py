from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.urls import reverse

from registration.models import Customer


def logging(request):
    form = AuthenticationForm(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('userProfile:userProfile'))
    else:
        return render(request, 'registration/login.html', {'form': form, 'error_message': "Неверно введено email или "
                                                                                          "пароль"})


def registration(request):
    return render(request, 'registration/registration.html')


def user_creating(request):
    if User.objects.filter(username=request.POST['login']):
        return render(request, 'registration/registration.html', {
            'error_message': "Пользователь с таким email уже существует",
        })
    else:
        user_data = [request.POST['login'], request.POST['password'],
                     request.POST['last_name'], request.POST['first_name']]
        customer_data = [request.POST['phone'], request.POST['district'], request.POST['street'], request.POST['house'],
                         request.POST['corp'], request.POST['flat'], request.POST['p_index']]

        user = User.objects.create_user(user_data[0], user_data[0], user_data[1], first_name=user_data[2],
                                        last_name=user_data[3])
        user.save()
        customer = Customer(user.id, user.id, customer_data[0], customer_data[1], customer_data[2],
                            customer_data[3], customer_data[4], customer_data[5], customer_data[6])
        customer.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('registration:registration_success'))


def registration_success(request):
    return render(request, 'registration/registration_success.html')
