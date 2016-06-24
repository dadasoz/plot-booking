import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, HttpResponse,render
from user_auth.models import User

from .helpers import LoginHelper
from plots.exceptions import AuthenticationFailed

from django.views.generic import View
from django.contrib.auth import authenticate


class LoginView(View):

    def post(self, request):
        post_data = request.POST
        try:
            username, user = self.clean_username(post_data.get("email", None))
        except ObjectDoesNotExist:
            return HttpResponse(status=401)

        password = post_data.get("password", None)

        helper = LoginHelper()
        data = helper.generate_oauth_token(request, username, password)

        if data.status_code == 200:
            content = json.loads(data.content)
            content.update(self.get_userinfo(user))          
            return HttpResponse(json.dumps(content),
                                content_type="application/json")
        else:
            return HttpResponse(status=401)

    def clean_username(self, username):
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                raise ObjectDoesNotExist
        else:
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist:
                raise ObjectDoesNotExist
        return user.username, user

    def get_userinfo(self, user):
        user_data = {
            "full_name": user.get_full_name(),
            "username": user.username,
            "is_active": user.is_active,
            "groups": [group.name for group in user.groups.all()],
            "email": user.email,
            "id": user.id,
            "user_category": user.user_category.name,
            "base_url": user.user_category.slug,
        }
        return user_data


def login_view(request):
    return render(request, "user_auth/login.html", {})
