from django.urls import path
from . views import *

urlpatterns=[
    path("saveuser/",saveuser,name='saveuser'),
    path("employeelist/",employeelist,name='employeelist'),
    path("updateEmployee/",updateEmployee,name='updateEmployee'),
    path("deleteEmployee/",deleteEmployee,name='deleteEmployee'),
    path("newEmployeeForm/",newEmployeeForm,name='newEmployeeForm'),
    path("updateEmployeeform/",updateEmployeeform,name='updateEmployeeform'),
    
]