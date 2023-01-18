from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminapp.forms import AdminShopUserUpdateForm, AdminShopUserCreateForm

# CRUD
from mainapp.models import ProductCategory


# Create your views here.

# @user_passes_test(lambda x: x.is_superuser)
# def index(request):
#     users = get_user_model().objects.all()
#     context = {
#         'page_title': 'админка/пользователи',
#         'object_list': users
#     }
#     return render(request, 'adminapp/index.html', context=context)


class SListView:
    pass


class ShopUserList(ListView):
    model = get_user_model()



# @user_passes_test(lambda x: x.is_superuser)
# def user_create(request):
#     if request.method == 'POST':
#         user_form = AdminShopUserCreateForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('myadmin:index'))
#     else:
#         user_form = AdminShopUserCreateForm()
#
#     context = {
#         'page_title': 'админка/пользователи/создание',
#         'form': user_form
#     }
#
#     return render(request, 'adminapp/user_update.html', context)


class ShopUserCreateView(CreateView):
    model = get_user_model()
    form_class = AdminShopUserCreateForm
    success_url = reverse_lazy('myadmin:index')


# @user_passes_test(lambda x: x.is_superuser)
# def user_update(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     if request.method == 'POST':
#         user_form = AdminShopUserUpdateForm(request.POST, request.FILES, instance=user)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('myadmin:index'))
#     else:
#         user_form = AdminShopUserUpdateForm(instance=user)
#
#     context = {
#         'page_title': 'админка/пользователи/редактирование',
#         'form': user_form
#     }
#
#     return render(request, 'adminapp/user_update.html', context)


class ShopUserUpdateView(UpdateView):
    model = get_user_model()
    form_class = AdminShopUserUpdateForm
    success_url = reverse_lazy('myadmin:index')
    pk_url_kwarg = 'user_pk'


# def user_delete(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     # user.delete()
#     if not user.is_active or request.method == 'POST':
#         if user.is_active:
#             user.is_active = False
#             user.save()
#         return HttpResponseRedirect(reverse('myadmin:index'))
#     context = {
#         'page_title': 'админка/пользователи/удаление',
#         'object': user
#     }
#     return render(request, 'adminapp/user_delete.html', context=context)


class ShopUserDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('myadmin:index')
    pk_url_kwarg = 'user_pk'


@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    context = {
        'page_title': 'админка/категории',
        'object_list': ProductCategory.objects.all()
    }
    return render(request, 'adminapp/categories.html', context=context)

