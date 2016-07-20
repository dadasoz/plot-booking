from django.conf.urls import url
from booking_api import views
urlpatterns = [
    url(r'^$', views.BookingList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.BookingDetail.as_view()),
    url(r'^create/$', views.CreateBooking.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$', views.BookingUpdate.as_view()),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.DestroyBooking.as_view()),
    url(r'^convert/(?P<pk>[0-9]+)/$', views.ConvertBooking.as_view()),
]
