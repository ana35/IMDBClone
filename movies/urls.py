from . import views
from django.urls import path, include

urlpatterns = [
    #path('movies/search', views.ListMoviesFilteredView.as_view(), name='movies-filtered'),
    path('movies/search', views.MoviesSearchView.as_view(), name='movies-filtered'),
    path('movies', views.FullMovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>', views.SingleMovieView.as_view()),
    path('rest-auth', include('rest_auth.urls')),
]
