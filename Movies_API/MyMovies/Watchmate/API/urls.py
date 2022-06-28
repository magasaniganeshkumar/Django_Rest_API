
from django.urls import path
from Watchmate.API.views import MovieListView, MovieDetailsView


urlpatterns = [
    path('movies-list/', MovieListView.as_view(), name='movies-list'),
    path('<int:pk>/', MovieDetailsView.as_view(), name='movie-details'),
]
