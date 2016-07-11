import json
import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import HttpResponse, render, redirect
from user_auth.models import User

from django.views.generic import View
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout

from oauthlib.common import generate_token
from oauth2_provider.models import Application, AccessToken


class LoginView(View):

    def post(self, request):
        post_data = request.POST
        try:
            username, user = self.clean_username(post_data.get("email", None))
        except ObjectDoesNotExist:
            return HttpResponse(status=401)

        password = post_data.get("password", None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                app = Application.objects.get(name="WebAPP")
                try:
                    old = AccessToken.objects.get(user=user, application=app)
                except:
                    pass
                else:
                    old.delete()

                token = generate_token()

                token = AccessToken.objects.get_or_create(user=user,
                                                          application=app,
                                                          expires=datetime.datetime.now() +
                                                          datetime.timedelta(
                                                              days=30),
                                                          token=token)[0]
                token_details = {"access_token": token.token, "token_type":
                                 "Bearer", "expires_in": 30, "scope": "read write"}
                content = self.get_userinfo(user)
                content.update(token_details)
                return HttpResponse(json.dumps(content),
                                    content_type="application/json")
            else:
                HttpResponse(status=401)
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
            "profile_photo": "{0}{1}".format(settings.MEDIA_URL, user.profile_photo),
        }
        return user_data

    def token_request(self, user):
        return Token.objects.create(user=user)


def login_view(request):
    return render(request, "user_auth/login.html", {})


def logout_view(request):
    logout(request)
    return redirect('user_auth:login')
