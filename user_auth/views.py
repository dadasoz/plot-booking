from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from user_auth.models import User


def loginview(request):
    return render(request, "user_auth/login.html", {})


def auth_and_login(request, onfail='/login/'):
    user = authenticate(
        username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect("/")
    else:
        return redirect(onfail)

def secured(request):
    return render_to_response("secure.html")
