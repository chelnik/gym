from django.urls import path
from .views import signup, login_view, profile_view, params_change, admin_panel_view, abon_view, new_abon_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('admin_panel/', admin_panel_view, name='admin_panel'),
    path('newparams/', params_change, name='newparams'),
    path('abon/', abon_view, name='abon'),
    path('new_abon/', new_abon_view, name='new_abon')
]
