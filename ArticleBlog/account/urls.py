from django.urls import path
from . import views



app_name = "account"

urlpatterns = [
    path("login", views.Login, name="login"),
    path("logout", views.Logout, name="logout"),
]