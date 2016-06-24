from django.conf.urls import url
from frontend.views import dashboard_view, projects_view

urlpatterns = [
    url(r'^$', dashboard_view, name="frontend_dashboard"),
    url(r'^projects/$', projects_view, name="projects"),
]
