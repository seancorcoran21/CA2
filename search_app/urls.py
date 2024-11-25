from django.urls import path
from .views import SearchResultsListView

app_name='search_app'

urlpatterns = [
        path('', SearchResultsListView.as_view(), name='searchResult'),
]
