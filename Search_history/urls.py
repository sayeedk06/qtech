from django.urls import path
from Search_history.views import SearchView,ajax_filter


urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('filter', ajax_filter, name='ajax_filter'),
]