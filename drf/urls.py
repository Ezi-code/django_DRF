
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("core.urls")),
    path('api/', include("core_api.urls", namespace='core')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
