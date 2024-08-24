from django.urls import path, include

urlpatterns = [
    path("investments/stocks/", include('modules.investments.stocks.api.urls')),    
]
