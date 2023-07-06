from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Author
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect




def Login(request):
    if request.user.is_authenticated == True:
        return redirect('home:home')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect("home:home")
    else:
        form = LoginForm()
    return render(request, "account/login.html", context={"form": form})



def Logout(request):
    logout(request)
    return redirect("home:home")