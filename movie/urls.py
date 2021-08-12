from django.urls import path

from movie.views import MovieTemplateView, MovieListView, TotalDetailView, SearchListView

app_name = 'movie'
urlpatterns = [
    path('', MovieTemplateView.as_view(), name='home'),
    path('catalog/<str:category>/', MovieListView.as_view(), name='catalog'),
    path('search-catalog/', SearchListView.as_view(), name='search-catalog'),
    path('catalog/<str:category>/<int:pk>/', TotalDetailView.as_view(), name='detail'),
]
