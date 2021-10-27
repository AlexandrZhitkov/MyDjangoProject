from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'tittle': 'GeekShop - Админ Панель'}
    return render(request, 'admins/index.html', context)


def admin_users_create(request):
    context = {'tittle': 'GeekShop - Создание пользователя'}
    return render(request, 'admins/admin-users-create.html', context)

def admin_users(request):
    context = {'tittle': 'GeekShop - Пользователи'}
    return render(request, 'admins/admin-users-read.html', context)

def admin_users_update(request):
    context = {'tittle': 'GeekShop - Обновление пользователя'}
    return render(request, 'admins/admin-users-update-delete.html', context)

def admin_users_delete(request):
    pass

