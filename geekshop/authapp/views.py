from django.contrib import auth
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserUpdateForm


def login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ShopUserLoginForm()

    context = {
        'page_title': 'вход в систему',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if user.send_verify_mail() == 0:
                return HttpResponseRedirect(reverse('auth:register'))
            return HttpResponseRedirect(reverse('main:index'))  # say ok
    else:
        form = ShopUserRegisterForm()

    context = {
        'page_title': 'регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def update(request):
    if request.method == 'POST':
        form = ShopUserUpdateForm(request.POST, request.FILES,
                                  instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
            # return HttpResponseRedirect(reverse('auth:update'))
    else:
        form = ShopUserUpdateForm(instance=request.user)

    context = {
        'page_title': 'редактирование',
        'form': form,
    }
    return render(request, 'authapp/update.html', context)


def verify(request, email, activation_key):
    user = get_user_model().objects.get(email=email)
    if user.activation_key == activation_key and not user.is_activation_key_expired():
        user.is_active = True
        user.save()
        auth.login(request, user)
    return render(request, 'authapp/verification.html')
