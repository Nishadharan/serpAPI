# serpapi_app/urls.py

from django.urls import path
from .views import SearchResultsAPIView

urlpatterns = [
    path('search/', SearchResultsAPIView.as_view(), name='search_results'),
   
]
