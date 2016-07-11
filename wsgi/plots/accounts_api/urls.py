from django.conf.urls import url
from accounts_api import views
urlpatterns = [
    url(r'^sales/$', views.ListSales.as_view()),
    url(r'^sales/create/$', views.CreateSales.as_view()),
    # url(r'^sales/udpate/(?P<pk>[0-9]+)/$', views.UpdateSales.as_view()),
    url(r'^sales/delete/(?P<pk>[0-9]+)/$', views.DestroySales.as_view()),
    url(r'^sales/(?P<pk>[0-9]+)/$', views.DetailsSales.as_view()),

    url(r'^emi/$', views.ListEMI.as_view()),
    url(r'^emi/create/$', views.CreateEMI.as_view()),
    #url(r'^emi/update/(?P<pk>[0-9]+)/$', views.UpdateEMI.as_view()),
    url(r'^emi/delete/(?P<pk>[0-9]+)/$', views.DestroyEMI.as_view()),
    url(r'^emi/(?P<pk>[0-9]+)/$', views.DetailsEMI.as_view()),
]
