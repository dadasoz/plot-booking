from django.conf.urls import url
from admin_api import views

urlpatterns = [
    url(r'^besic/$', views.CompanyDetail.as_view()),
    url(r'^besic/update/$', views.CompanyUpdate.as_view()),

    url(r'^commission/$', views.CommissionSettingsDetail.as_view()),
    url(r'^commission/update/$', views.CommissionSettingsUpdate.as_view()),
]
