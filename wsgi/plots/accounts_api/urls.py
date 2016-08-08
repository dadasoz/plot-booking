from django.conf.urls import url
from accounts_api import views
urlpatterns = [
    url(r'^sales/$', views.ListSales.as_view()),
    url(r'^sales/create/$', views.CreateSales.as_view()),
    url(r'^sales/update/(?P<pk>[0-9]+)/$', views.UpdateSales.as_view()),
    url(r'^sales/delete/(?P<pk>[0-9]+)/$', views.DestroySales.as_view()),
    url(r'^sales/(?P<pk>[0-9]+)/$', views.DetailsSales.as_view()),

    url(r'^emi/$', views.ListEMI.as_view()),
    url(r'^emi/create/$', views.CreateEMI.as_view()),
    url(r'^emi/update/(?P<pk>[0-9]+)/$', views.UpdateEMI.as_view()),
    url(r'^emi/pay/(?P<pk>[0-9]+)/$', views.PayEMI.as_view()),
    url(r'^emi/delete/(?P<pk>[0-9]+)/$', views.DestroyEMI.as_view()),
    url(r'^emi/(?P<pk>[0-9]+)/$', views.DetailsEMI.as_view()),

    url(r'^transactions/$', views.ListTransactions.as_view()),
    url(r'^transactions/create/$', views.CreateTransactions.as_view()),
    url(r'^transactions/update/(?P<pk>[0-9]+)/$', views.UpdateTransactions.as_view()),
    url(r'^transactions/update/status/(?P<pk>[0-9]+)/$', views.UpdateTransactionStatus.as_view()),
    url(r'^transactions/delete/(?P<pk>[0-9]+)/$', views.DestroyTransactions.as_view()),
    url(r'^transactions/(?P<pk>[0-9]+)/$', views.DetailsTransactions.as_view()),

    url(r'^expenses/$', views.ListExpenses.as_view()),
    url(r'^expenses/(?P<pk>[0-9]+)/$', views.DetailsExpenses.as_view()),
    url(r'^expenses/create/$', views.CreateExpenses.as_view()),
    url(r'^expenses/update/(?P<pk>[0-9]+)/$', views.UpdateExpenses.as_view()),
    url(r'^expenses/delete/(?P<pk>[0-9]+)/$', views.DestroyExpenses.as_view()),

]
