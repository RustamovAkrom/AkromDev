from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from .schema import swagger_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls, name="admin_panel"),
    path("", include("apps.akromdev.urls")),
    path("users/", include("apps.users.urls")),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

