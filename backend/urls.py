from django.conf.urls import url
from frontend.views import dashboard_view

urlpatterns = [
    url(r'^$', dashboard_view, name="backend_dashboard"),
]
