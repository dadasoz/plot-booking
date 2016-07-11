from django.conf.urls import url
from customer_api import views
urlpatterns = [
    url(r'^$', views.CustomerList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    url(r'^create/$', views.CreateCustomer.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$', views.CustomerUpdate.as_view()),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DestroyCustomer.as_view()),
]
