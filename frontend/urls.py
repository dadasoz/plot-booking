from django.conf.urls import url
from frontend import views

urlpatterns = [
    url(r'^$', views.dashboard_view, name="frontend_dashboard"),
    url(r'^projects/$', views.projects_view, name="projects"),
    url(r'^plots/$', views.plots_view, name="plots"),
    url(r'^customers/$', views.customers_view, name="customers"),
]
