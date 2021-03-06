"""plots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from plots.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^dev-admin/', admin.site.urls),
    url(r'^auth/', include('user_auth.urls', namespace="user_auth")),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^frontend/', include('frontend.urls', namespace="frontend")),
    url(r'^backend/', include('backend.urls', namespace="backend")),
    url(r'^api/admin/', include('admin_api.urls', namespace="admin_api")),
    url(r'^api/projects/', include('projects_api.urls', namespace="projects_api")),
    url(r'^api/booking/', include('booking_api.urls', namespace="booking_api")),
    url(r'^api/customers/', include('customer_api.urls', namespace="customer_api")),
    url(r'^api/accounts/', include('accounts_api.urls', namespace="accounts_api")),
    url(r'^api/agents/', include('agents_api.urls', namespace="agents_api")),
    url(r'^api/feedback/', include('feedback_api.urls', namespace="feedback_api")),
]


if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
