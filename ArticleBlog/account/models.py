from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify




class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    image = models.FileField(upload_to="images/Authors")
    nickname = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=30, unique=True, editable=False)

    def __str__(self):
        return self.nickname
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nickname)
        super(Author, self).save(*args, **kwargs)