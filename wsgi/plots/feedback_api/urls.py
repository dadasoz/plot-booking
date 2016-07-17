from django.conf.urls import url
from feedback_api import views
urlpatterns = [
    url(r'^$', views.FeedbackList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.FeedbackDetail.as_view()),
    url(r'^create/$', views.CreateFeedback.as_view()),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DestroyFeedback.as_view()),
]
