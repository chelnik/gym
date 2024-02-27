from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import SignUpForm, LoginForm, ParamsForm, UserAbonForm, AdminAbonForm
from .models import Params, UserProfile, Aboniment
from .decorators import user_required, superuser_required
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Создаем пользователя
            user = form.save()

            # Создаем профиль пользователя
            UserProfile.objects.create(user=user)

            # Авторизуем пользователя
            login(request, user)

            # Перенаправляем на страницу входа (или куда вам нужно)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@superuser_required
def admin_panel_view(request):
    # Исключаем суперпользователей из выборки
    user_profiles = UserProfile.objects.filter(is_superuser=False)

    # Передаем данные в контекст шаблона
    context = {
        'user_profiles': user_profiles,
        'params_list': Params.objects.all(),  # Передаем все параметры
        'aboniment_list': Aboniment.objects.all(),  # Передаем все абонементы
    }

    # Отображаем шаблон с переданными данными
    return render(request, 'accounts/admin_panel.html', context)




def profile_view(request):
    if request.user.is_superuser:
        return redirect('admin_panel')

    @user_required
    def inner_profile_view(request):
        user_profile = UserProfile.objects.get(user=request.user)
        data = {
            'params': Params.objects.filter(user_profile=user_profile),
            'aboniment': user_profile.aboniment,
            'user_profile': user_profile
        }
        return render(request, 'accounts/profile.html', data)

    return inner_profile_view(request)


@login_required
def params_change(request):
    try:
        params_instance = Params.objects.get(user_profile=request.user.userprofile)
    except Params.DoesNotExist:
        params_instance = Params(user_profile=request.user.userprofile)

    if request.method == 'POST':
        form = ParamsForm(request.POST, instance=params_instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ParamsForm(instance=params_instance)

    data = {
        'form': form
    }
    return render(request, 'accounts/newparams.html', data)


def abon_view(request):
    abon = Aboniment.objects.all()
    return render(request, 'accounts/abon.html', {'abon':abon})


def new_abon_view(request):
    # Обработка формы для администратора
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AdminAbonForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data['user']
                aboniment = form.cleaned_data['aboniment']

                user_profile = UserProfile.objects.get(user=user)
                user_profile.aboniment = aboniment
                user_profile.save()

                return redirect('admin_panel')
        else:
            form = AdminAbonForm()

    # Обработка формы для обычного пользователя
    else:
        if request.method == 'POST':
            form = UserAbonForm(request.POST)
            if form.is_valid():
                user_profile = UserProfile.objects.get(user=request.user)
                user_profile.aboniment = form.cleaned_data['aboniment']
                user_profile.save()

                return redirect('profile')
        else:
            form = UserAbonForm()

    return render(request, 'accounts/new_abon.html', {'form': form})