from django.conf.urls import url, include
from sales import views

urlpatterns = [
    url(r'^charge/$', views.charge, name="charge"),
    url(r'^charges/$', views.charges, name="charges"),
]