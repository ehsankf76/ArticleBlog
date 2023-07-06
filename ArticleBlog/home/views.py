from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Article



def home(request):
    articles = Article.objects.all()
    return render(request, "home/home.html", context={"articles": articles})