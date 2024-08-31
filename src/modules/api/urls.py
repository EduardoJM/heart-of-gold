from django.urls import path, include

urlpatterns = [
    path("auth/", include("modules.api.authentication.urls")),
    path("investments/", include('modules.investments.urls')),
]
