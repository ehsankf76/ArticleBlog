from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from .forms import AddArticleForm, EditArticleForm
from .models import Article, Category
from account.models import Author
from django.core.paginator import Paginator

# ***********************************************************

class ArticlesListView(ListView):
    paginate_by = 2
    model = Article

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["txt1"] = "Recent articles"
        context["txt2"] = "Our recent blog entries"
        return context

# ***********************************************************

def CategoryListView(request, slug):
    category = Category.objects.get(slug=slug)
    object_list = category.articles.all()
    paginator = Paginator(object_list, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    txt1 = "Articles of this category:"
    txt2 = category.title
    return render(request, "blog/article_list.html", context={"object_list": object_list, "txt1": txt1, "txt2": txt2, "page_obj": page_obj})

# ***********************************************************

def AuthorArticlesListView(request, slug):
    author = Author.objects.get(slug=slug)
    object_list = author.articles.all()
    paginator = Paginator(object_list, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    txt1 = "Articles of this author:"
    txt2 = author.nickname
    return render(request, "blog/article_list.html", context={"txt1": txt1, "txt2": txt2, "page_obj": page_obj})

# ***********************************************************

def AuthorListView(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    txt1 = "All authors"
    txt2 = "All our authors"
    return render(request, "blog/authors_list.html", context={"object_list": authors, "txt1": txt1, "txt2": txt2, "page_obj": page_obj})

# ***********************************************************

class ArticleDetailView(DetailView):
    model = Article

# ***********************************************************

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
    
# ***********************************************************

def EditArticleView(request, slug):
    instance = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        form = EditArticleForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("blog:article-detail", slug=slug)
    
    else:
        if (not request.user.is_authenticated) or instance.author != request.user.author:
            return redirect("home:home")
        form = EditArticleForm(instance=instance)

    return render(request, 'blog/add_article.html', {'form':form})