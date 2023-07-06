from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Article



def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.order_by("-created")[:3]
    return render(request, "home/home.html", context={"articles": articles, "recent_articles":recent_articles})