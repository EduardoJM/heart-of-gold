from django.urls import path, include

urlpatterns = [
    path("investments/", include('modules.investments.urls')),
]
