from django import forms
from django.forms import ValidationError, ModelForm, Textarea
from .models import Article
from account.models import Author



class AddArticleForm(ModelForm):
    
    class Meta:
        model = Article
        fields = ["image", "title", "body", "category"]
        widgets = {
            'title': Textarea(attrs={'class': 'input100', 'style': 'width:390px; height:30px'}),
            'body': Textarea(attrs={'class': 'input100', 'style': 'width:390px; height:300px'}),
        }