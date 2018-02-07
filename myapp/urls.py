from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^register/', views.save, name='register'),
    url(r'^login/', views.loginview, name='login'),
    url(r'^accounts/login/', views.loginview, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^forget/', views.forget_password, name="forget"),
    url(r'^home', views.home, name="profile"),
    url(r'^courses/', views.courses, name="courses"),
    url(r'^academics/', views.academics, name="academics"),
    url(r'^events/', views.events, name="events"),
    url(r'^library/', views.library, name="library"),
    url(r'^services/', views.services, name="services"),
    url(r'^maps/', views.maps, name="maps"),
    url(r'^calendar/', views.calendar, name="calendar"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
