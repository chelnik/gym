# Generated by Django 4.2.7 on 2023-12-04 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_aboniment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboniment',
            name='anons',
        ),
    ]
