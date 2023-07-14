from django.urls import path
from . import views




app_name = "blog"

urlpatterns = [
    path("all_articles", views.ArticlesListView.as_view(), name="all-articles"),
    path("search_articles", views.ArticleSearchView, name="search-articles"),
    path("authors", views.AuthorListView, name="all-authors"),
    path("add_article", views.AddArticleView.as_view(), name="add-article"),
    path("edit_article/<slug:slug>", views.EditArticleView, name="edit-article"),
    path("<slug:slug>", views.ArticleDetailView, name="article-detail"),
    path("articles/<slug:slug>", views.CategoryListView, name="category-list"),
    path("authors/<slug:slug>", views.AuthorArticlesListView, name="author-articles"),
]