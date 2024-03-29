# Generated by Django 4.2.7 on 2023-12-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_params_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboniment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.CharField(max_length=15, verbose_name='Цена')),
                ('anons', models.CharField(max_length=500, verbose_name='Описание абонимента')),
            ],
            options={
                'verbose_name': 'Абонимент',
                'verbose_name_plural': 'Абонименты',
            },
        ),
    ]
