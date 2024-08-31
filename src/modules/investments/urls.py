from django.urls import path, include

urlpatterns = [
    path("funds/", include("modules.investments.funds.urls")),
    path("treasury/", include('modules.investments.treasury.urls')),
    path("", include('modules.investments.stocks.api.urls')),
]