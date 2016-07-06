from django.conf.urls import url
from accounts_api import views
urlpatterns = [
    url(r'^sales/$', views.ListSales.as_view()),
    url(r'^emi/(?P<sales_id>[0-9]+)/$', views.ListEMI.as_view()),
    # url(r'^sales/(?P<pk>[0-9]+)/$', views.BookingDetail.as_view()),
    url(r'^sales/create/$', views.CreateSales.as_view()),
    # url(r'^sales/update/(?P<pk>[0-9]+)/$', views.BookingUpdate.as_view()),
    # url(r'^sales/delete/(?P<pk>[0-9]+)/$', views.DestroyBooking.as_view()),
]
