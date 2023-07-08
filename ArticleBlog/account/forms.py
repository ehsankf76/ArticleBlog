from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError, ModelForm, Textarea
from .models import Author
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get("username"), password=self.cleaned_data.get("password"))
        if user is not None:
            return self.cleaned_data.get("password")
        raise ValidationError("username or password is wrong", code="invalid_info")



class RegisterFormUser(ModelForm):
    
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            'username': Textarea(attrs={'class': 'input100'}),
            'password': forms.PasswordInput(attrs={'class': 'input100'}),
        }

    def save(self, commit=True):
        user = super(RegisterFormUser, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class RegisterFormAuthor(ModelForm):
    
    class Meta:
        model = Author
        exclude = ["user"]
        widgets = {
            'first_name': Textarea(attrs={'class': 'input100'}),
            'last_name': Textarea(attrs={'class': 'input100'}),
            'email': forms.EmailInput(attrs={'class': 'input100'}),
            'phone_number': forms.Textarea(attrs={'class': 'input100'}),
            'nickname': forms.Textarea(attrs={'class': 'input100'}),
        }