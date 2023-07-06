from django.urls import path
from . import views




app_name = "blog"

urlpatterns = [
    path("all_articles", views.ArticlesListView.as_view(), name="all-articles"),
    path("authors", views.AuthorListView, name="all-authors"),
    path("<slug:slug>", views.ArticleDetailView.as_view(), name="article-detail"),
    path("articles/<slug:slug>", views.CategoryListView, name="category-list"),
    path("authors/<slug:slug>", views.AuthorArticlesListView, name="author-articles"),
]