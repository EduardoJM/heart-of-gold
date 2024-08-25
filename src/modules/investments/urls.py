from django.urls import path, include

urlpatterns = [
    path("treasury/", include('modules.investments.treasury.urls')),
    path("", include('modules.investments.stocks.api.urls')),
]