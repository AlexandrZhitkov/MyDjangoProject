from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from users.models import User
from admins.forms import UserAdminRegistrationForm


def index(request):
    context = {'tittle': 'GeekShop - Админ Панель'}
    return render(request, 'admins/index.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'tittle': 'GeekShop - Создание пользователя', 'form':form}
    return render(request, 'admins/admin-users-create.html', context)

def admin_users(request):
    context = {
        'tittle': 'GeekShop - Пользователи',
        'users': User.objects.all(),
        }
    return render(request, 'admins/admin-users-read.html', context)

def admin_users_update(request):
    context = {'tittle': 'GeekShop - Обновление пользователя'}
    return render(request, 'admins/admin-users-update-delete.html', context)

def admin_users_delete(request):
    pass

