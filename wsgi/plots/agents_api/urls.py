from django.conf.urls import url
from agents_api import views
urlpatterns = [
    url(r'^$', views.AgentList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.AgentDetail.as_view()),
    url(r'^create/$', views.CreateAgent.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$', views.AgentUpdate.as_view()),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DestroyAgent.as_view()),
]
