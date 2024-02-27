from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Params, Aboniment
from django.forms import ModelForm, TextInput, NumberInput


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ParamsForm(ModelForm):
    class Meta:
        model = Params
        fields = ['target', 'height', 'weight', 'neck', 'hands', 'forearms', 'chest', 'waist', 'pelvis', 'hips', 'shin','ankles']

        widgets = {
            "target": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша цель'
            }),
            "height": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Рост'
            }),
            "weight": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вес'
            }),
            "neck": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Шея'
            }),
            "hands": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Руки'
            }),
            "forearms": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Предплечья'
            }),
            "chest": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Грудь'
            }),
            "waist": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Талия'
            }),
            "pelvis": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Таз'
            }),
            "hips": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Бедра'
            }),
            "shin": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Голени'
            }),
            "ankles": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Лодыжки'
            })
        }


class AdminAbonForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=False), label='Пользователь')
    aboniment = forms.ModelChoiceField(queryset=Aboniment.objects.all(), label='Абонемент')


class UserAbonForm(forms.Form):
    aboniment = forms.ModelChoiceField(queryset=Aboniment.objects.all(), label='Абонемент')