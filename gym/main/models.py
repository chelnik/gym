from django.db import models


class Coaches(models.Model):
    fio = models.CharField('ФИО', max_length=50)
    obj_title = models.CharField('направление', max_length=50)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'



class AboutGym(models.Model):
    title = models.CharField('Название зоны', max_length=50)
    anons = models.CharField('Тренажеры', max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О зале'
        verbose_name_plural = 'О зале'