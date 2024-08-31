from django.urls import path, include, reverse
from django.shortcuts import redirect

urlpatterns = [
    path("auth/", include("modules.api.authentication.urls")),
    path("investments/", include('modules.investments.urls')),
    path("docs/", include('modules.api.docs.urls')),
    path('', lambda _: redirect(reverse('swagger-ui')))
]
