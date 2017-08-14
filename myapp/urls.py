from django.conf.urls import url
from .  import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    url(r'^register/',views.save,name='register'),
    url(r'^login/',views.loginview,name='login'),
    url(r'^logout/',views.logout_view,name='logout'),
    url(r'^forget/',views.forget_password,name="forget"),
    url(r'^profile/',views.update_profile,name="profile"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
