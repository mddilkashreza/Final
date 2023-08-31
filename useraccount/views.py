from django.shortcuts import render, reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from useraccount.forms import CustomLoginForm,SignUpForm
from useraccount.models import User




def user_login(request):
    form = CustomLoginForm(request.POST or None)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("blog:index"))
        else:
            errors = form.get_invalid_login_error()
            for error in errors:
                messages.add_message(request, messages.ERROR, ("Sorry but you cant"))
    context = {"form": form}
    return render(request, 'login.html', context)



def user_signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("useraccount:user_login"))
    messages.success(request, 'Register Succesfully')
    context = {"form": form}
    return render(request, "signup.html", context)



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("useraccount:user_login"))





