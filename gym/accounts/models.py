from django.contrib.auth.models import User
from django.db import models


class Aboniment(models.Model):
    title = models.CharField('Название', max_length=50)
    price = models.CharField('Цена', max_length=15)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_superuser = models.BooleanField(default=False)
    aboniment = models.ForeignKey(Aboniment, on_delete=models.SET_NULL, blank=True, null=True)
    buy_day = models.CharField('Дата приобретения', max_length=15, default = '')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Params(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    target = models.CharField('Цель', max_length=50, null=True, blank=True, default='')
    height = models.FloatField('Рост', null=True, blank=True)
    weight = models.FloatField('Вес', null=True, blank=True)
    neck = models.FloatField('Шея', null=True,  blank=True)
    hands = models.FloatField('Руки', null=True,  blank=True)
    forearms = models.FloatField('Предплечья', null=True,  blank=True)
    chest = models.FloatField('Грудь', null=True,  blank=True)
    waist = models.FloatField('Талия', null=True,  blank=True)
    pelvis = models.FloatField('Таз', null=True,  blank=True)
    hips = models.FloatField('Бедра', null=True,  blank=True)
    shin = models.FloatField('Голень', null=True,  blank=True)
    ankles = models.FloatField('Лодыжки', null=True,  blank=True)

    def __str__(self):
        return f"{self.height} - {self.user_profile.user.username}" if self.user_profile else str(self.height)


    class Meta:
        verbose_name = 'Параметры'
        verbose_name_plural = 'Параметры'
