from django.conf.urls import url
from projects_api import views
urlpatterns = [
    url(r'^$', views.ProjectsList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectsDetail.as_view()),
]
