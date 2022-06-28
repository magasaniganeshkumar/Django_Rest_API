
from django.urls import path
from Watchmate.views import movies_list, movie_details


urlpatterns = [
    path('movies-list/', movies_list, name='movies_list'),
    path('<int:movie_id>/', movie_details, name='movie-details'),
]
