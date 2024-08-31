from django.shortcuts import redirect
from django.urls import include, path, reverse

urlpatterns = [
    path("auth/", include("modules.api.authentication.urls")),
    path("users/", include("modules.users.urls")),
    path("investments/", include("modules.investments.urls")),
    path("docs/", include("modules.api.docs.urls")),
    path("", lambda _: redirect(reverse("swagger-ui"))),
]
