from django.conf.urls import patterns, include, url
from user_auth.views import login_view, LoginView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^login/$', login_view),
    url(r'^login-validate/$', LoginView.as_view(), name='login_validate'),
]
