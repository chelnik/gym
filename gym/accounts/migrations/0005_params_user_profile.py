# Generated by Django 4.2.7 on 2023-12-03 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_userprofile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='params',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
    ]
