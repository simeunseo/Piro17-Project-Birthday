# Create your views here.
from django.shortcuts import redirect, render
from django.views import View
from . import forms
# from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class LoginView(View):
    forms 
    def get(self, request):
        form = forms.LoginForm()
        ctx = {"form": form}
        return render(request, "./users/login.html", ctx)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "./posts/main.html")

        return render(request, "./users/login.html", {"form": form})

@login_required
def log_out(request):
    logout(request)
    return redirect("posts:main")


def sign_up(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, "./posts/main.html")
        return redirect("users:sign_up")
    else:
        form = forms.SignupForm()
        return render(request, "./users/signup.html", {"form": form})
    
    