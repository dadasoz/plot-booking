from django.conf.urls import url
from frontend import views

urlpatterns = [
    url(r'^$', views.dashboard_view, name="frontend_dashboard"),
    url(r'^projects/$', views.projects_view, name="projects"),
    url(r'^plots/$', views.plots_view, name="plots"),
    url(r'^customers/$', views.customers_view, name="customers"),
    url(r'^bookings/$', views.bookings_view, name="bookings"),
    url(r'^bookings/edit/(?P<pk>[0-9]+)/$', views.bookings_edit, name="bookings_edit"),

    url(r'^accounts/$', views.accounts_view, name="accounts"),
    url(r'^accounts/sales/$', views.accounts_sales_view, name="sales"),
    url(r'^accounts/sales/edit/(?P<pk>[0-9]+)/$', views.sales_edit, name="sales_edit"),
    url(r'^accounts/expenses/$', views.accounts_expenses_view, name="expenses"),

    url(r'^users/$', views.users_view, name="users"),
    url(r'^feedback/$', views.feedback_view, name="feedback"),
    url(r'^reports/$', views.reports_view, name="reports"),

    url(r'^agents/$', views.agents_view, name="agents"),

    url(r'^admin/settings/$', views.admin_settings_view, name="admin_settings_view"),
]
