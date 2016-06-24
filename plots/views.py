from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return render(request, "user_auth/login.html", {})
