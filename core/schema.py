from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    info=openapi.Info(
        title="AkromDev Api",
        default_version="v1",
        terms_of_service="https://www.yourappp.com/terms/",
        contact=openapi.Contact(email="akromjonrustamov56@gmail.com"),
        license=openapi.License(name="Your license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
