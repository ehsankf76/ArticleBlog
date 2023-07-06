from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article



class ArticlesListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["recent_articles"] = Article.objects.order_by("-created")[:3]
        return context
    


class ArticleDetailView(DetailView):
    model = Article