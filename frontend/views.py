from django.shortcuts import render

# Create your views here.


def dashboard_view(request):
    return render(request, "frontend/dashboard.html", {})


def projects_view(request):
    return render(request, "frontend/projects.html", {})
