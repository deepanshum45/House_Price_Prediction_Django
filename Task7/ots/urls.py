from django.urls import path
from . views import *
urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('test1/', test1, name='test1'),
    path('test3/', test3, name='test3'),
    path('test5/', test5, name='test5'),
    path('history/', history, name='history'),]

