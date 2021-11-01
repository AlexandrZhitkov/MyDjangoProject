from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm

@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'tittle': 'GeekShop - Админ Панель'}
    return render(request, 'admins/index.html', context)

@user_passes_test(lambda u: u.is_staff)
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

@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {
        'tittle': 'GeekShop - Пользователи',
        'users': User.objects.all(),
        }
    return render(request, 'admins/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, id):
    selected_user =  User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'tittle': 'GeekShop - Обновление пользователя',
        'form': form,
        'selected_user' : selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.safe_delete()
    return HttpResponseRedirect(reverse('admins:admin_users'))

