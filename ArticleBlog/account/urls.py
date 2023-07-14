from django.urls import path
from . import views



app_name = "account"

urlpatterns = [
    path("register", views.Register, name="register"),
    path("edit_user/<slug:slug>", views.EditUser, name="edit-user"),
    path("login", views.Login, name="login"),
    path("logout", views.Logout, name="logout"),
]