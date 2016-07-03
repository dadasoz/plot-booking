from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def validate_cookie(func):
    def decorated(request, *args, **kwargs):
        if request.COOKIES.get('login_info'):
            return func(request, *args, **kwargs)
        else:
            return redirect("/auth/logout/")
    return decorated

# Create your views here.

@login_required(login_url='/auth/login/')
@validate_cookie
def dashboard_view(request):
    return render(request, "frontend/dashboard.html", {})

@login_required(login_url='/auth/login/')
@validate_cookie
def projects_view(request):
    return render(request, "frontend/projects.html", {})

@login_required(login_url='/auth/login/')
@validate_cookie
def plots_view(request):
    return render(request, "frontend/plots.html", {})

@login_required(login_url='/auth/login/')
@validate_cookie
def customers_view(request):
    return render(request, "frontend/customers/index.html", {})

@login_required(login_url='/auth/login/')
@validate_cookie
def bookings_view(request):
    return render(request, "frontend/bookings/index.html", {})