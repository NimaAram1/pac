from django.urls import path 
from . import views


app_name = "account"

urlpatterns = [
    path("login",views.user_login.as_view(), name="login"),
    path("logout",views.user_logout.as_view(), name="logout"),
    path("register",views.user_register.as_view(), name="register"),
]
