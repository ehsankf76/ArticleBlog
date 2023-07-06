from django.urls import path
from . import views




app_name = "blog"

urlpatterns = [
    path("all_articles", views.ArticlesListView.as_view(), name="all-articles"),
]