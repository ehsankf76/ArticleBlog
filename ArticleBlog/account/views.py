from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Author
from .forms import LoginForm, RegisterFormAuthor, RegisterFormUser
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect




def Login(request):
    if request.user.is_authenticated == True:
        return redirect('home:home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get("username"))
            login(request, user)
            return redirect("home:home")
    else:
        form = LoginForm()
    return render(request, "account/login.html", context={"form": form})



def Logout(request):
    logout(request)
    return redirect("home:home")



def Register(request):
    if request.user.is_authenticated == True:
        return redirect('home:home')
    
    if request.method == "POST":
        form_user = RegisterFormUser(request.POST)
        form_author = RegisterFormAuthor(request.POST, request.FILES)
        if form_user.is_valid() and form_author.is_valid():
            # form_user
            user = form_user.save()

            # form_author
            author = form_author.save(commit=False)
            author.user = user
            author.save()

            login(request, user)
            return redirect("home:home")
    else:
        form_user = RegisterFormUser()
        form_author = RegisterFormAuthor()
    return render(request, "account/register.html", context={"form_user":form_user, "form_author":form_author})