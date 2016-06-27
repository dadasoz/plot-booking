from django.conf.urls import url
from projects_api import views
urlpatterns = [
    url(r'^$', views.ProjectsList.as_view()),
    url(r'^for-plots/$', views.ProjectsListForPlots.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectsDetail.as_view()),
    url(r'^plots/$', views.PlotList.as_view()),
    url(r'^plots/(?P<pk>[0-9]+)/$', views.PlotDetail.as_view()),
]
