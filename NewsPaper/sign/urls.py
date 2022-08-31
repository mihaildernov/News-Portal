from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from .views import upgrade_me_authors, upgrade_me_sport, upgrade_me_business, upgrade_me_education, upgrade_me_entertainment


urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'sign/signup.html'),
         name='signup'),
    path('upgrade/', upgrade_me_authors, name = 'upgrade'),
    path('upgrade2/', upgrade_me_sport, name = 'upgrade2'),
    path('upgrade3/', upgrade_me_business, name = 'upgrade3'),
    path('upgrade4/', upgrade_me_education, name = 'upgrade4'),
    path('upgrade5/', upgrade_me_entertainment, name = 'upgrade5'),
]