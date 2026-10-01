from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('saveuser/', views.saveuser, name='saveuser'),
    path('login/', views.login, name='login'),
    path( 'loginvalidation/',views.loginvalidation,name='loginvalidation'),
    path('srf/', views.srf, name='srf'),
    path('spp/', views.spp, name='spp'),
    path('result/', views.result, name='result'),
]
