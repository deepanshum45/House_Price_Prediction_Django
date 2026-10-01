from django.urls import path
from App2 import views

urlpatterns=[
    path("instagram/",views.instagram),
    path("linkedin/",views.linkdin),
]