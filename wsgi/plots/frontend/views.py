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


@login_required(login_url='/auth/login/')
@validate_cookie
def bookings_edit(request, pk):
    return render(request, "frontend/bookings/edit.html", {'pk': pk})

@login_required(login_url='/auth/login/')
@validate_cookie
def accounts_view(request):
    return render(request, "frontend/accounts/index.html", {})

@login_required(login_url='/auth/login/')
@validate_cookie
def accounts_sales_view(request):
    return render(request, "frontend/accounts/sales/index.html", {})


@login_required(login_url='/auth/login/')
@validate_cookie
def sales_edit(request, pk):
    return render(request, "frontend/accounts/sales/edit.html", {'pk': pk})

@login_required(login_url='/auth/login/')
@validate_cookie
def accounts_expenses_view(request):
    return render(request, "frontend/accounts/expenses/index.html", {})


@login_required(login_url='/auth/login/')
@validate_cookie
def users_view(request):
    return render(request, "frontend/users/index.html", {})


@login_required(login_url='/auth/login/')
@validate_cookie
def feedback_view(request):
    return render(request, "frontend/feedback/index.html", {})


@login_required(login_url='/auth/login/')
@validate_cookie
def reports_view(request):
    return render(request, "frontend/reports/index.html", {})



@login_required(login_url='/auth/login/')
@validate_cookie
def agents_view(request):
    return render(request, "frontend/agents/index.html", {})


@login_required(login_url='/auth/login/')
@validate_cookie
def admin_settings_view(request):
    return render(request, "frontend/admin/settings.html", {})