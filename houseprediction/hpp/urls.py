from django.urls import path
from hpp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("users/", views.userlist, name="userlist"),
    path("update/<int:id>/", views.update_user, name="update_user"),
    path("delete/<int:id>/", views.delete_user, name="delete_user"),
    path("logout/", views.logout, name="logout"),
    path("predict/", views.predict_price, name="predict_price"),
]