from django.db import models
from django.template.defaultfilters import slugify
from account.models import Author
from django.urls import reverse



class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True, editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)



class Article(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True, editable=False)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    category = models.ManyToManyField(Category, related_name="articles")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:article-detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)