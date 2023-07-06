from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Category
from account.models import Author



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