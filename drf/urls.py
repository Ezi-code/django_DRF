from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("api/", include("core_api.urls", namespace="core_api")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
