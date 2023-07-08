from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView
from .forms import AddArticleForm
from .models import Article, Category
from account.models import Author
from django.http import Http404, HttpRequest, HttpResponse



class ArticlesListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["txt1"] = "Recent articles"
        context["txt2"] = "Our recent blog entries"
        return context



def CategoryListView(request, slug):
    category = Category.objects.get(slug=slug)
    object_list = category.articles.all()
    txt1 = "Articles of this category:"
    txt2 = category.title
    return render(request, "blog/article_list.html", context={"object_list": object_list, "txt1": txt1, "txt2": txt2})



def AuthorArticlesListView(request, slug):
    author = Author.objects.get(slug=slug)
    object_list = author.articles.all()
    txt1 = "Articles of this author:"
    txt2 = author.nickname
    return render(request, "blog/article_list.html", context={"object_list": object_list, "txt1": txt1, "txt2": txt2})



def AuthorListView(request):
    authors = Author.objects.all()
    txt1 = "All authors"
    txt2 = "All our authors"
    return render(request, "blog/authors_list.html", context={"object_list": authors, "txt1": txt1, "txt2": txt2})



class ArticleDetailView(DetailView):
    model = Article



class AddArticleView(FormView):
    template_name = "blog/add_article.html"
    form_class = AddArticleForm
    success_url = "home:home"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.success_url)
    
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user.author
            article.save()
            form.save_m2m()
            return redirect(self.success_url)

        return render(request, self.template_name, {"form": form})