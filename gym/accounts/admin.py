from django.contrib import admin
from .models import Params, UserProfile, Aboniment

admin.site.register(UserProfile)
admin.site.register(Aboniment)
admin.site.register(Params)