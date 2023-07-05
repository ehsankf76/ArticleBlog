from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="images/profiles")
    nickname = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nickname
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Profile, self).save(*args, **kwargs)