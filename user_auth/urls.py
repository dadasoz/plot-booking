from django.conf.urls import patterns, include, url
from user_auth.views import loginview, auth_and_login, secured

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^login/', loginview),
    url(r'^auth/', auth_and_login),
#    url(r'^signup/', sign_up_in),
    url(r'^$', secured),
]
