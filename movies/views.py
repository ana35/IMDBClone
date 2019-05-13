from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

# Create your views here.
class MoviesSearchView(ListAPIView):
    """View to display filtered movie list on the basis of filters."""

    allowed_methods = ['GET']
    serializer_class = MovieSerializer
    model = serializer_class.Meta.model
    filter_fields = ('name', 'director', 'genre', 'imdb_score', 'popularity')
    #paginate_by = 10

    def get_queryset(self):
        """Method to put filter on the data"""

        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = self.model.objects.filter(name__icontains=name)
            orderBy = 'name'

        director = self.request.query_params.get('director', None)
        if director is not None:
            queryset = self.model.objects.filter(director__icontains=director)
            orderBy = 'director'

        genre = self.request.query_params.get('genre', None)
        if genre is not None:
            queryset = self.model.objects.filter(genre__name__icontains=genre)
            orderBy = 'genre'

        rating = self.request.query_params.get('rating', None)
        if rating is not None:
            queryset = self.model.objects.filter(imdb_score__gte=rating)
            orderBy = 'imdb_score'

        popularity = self.request.query_params.get('popularity', None)
        if popularity is not None:
            queryset = self.model.objects.filter(popularity__gte=popularity)
            orderBy = 'popularity'

        return queryset.order_by(orderBy)


class FullMovieListView(ListCreateAPIView):
    """This class return full movie list"""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        """Method to create movie"""

        serializer.save()


class SingleMovieView(RetrieveUpdateDestroyAPIView):
    """Class used for PUT, PATCH and DELETE methods."""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser,]


# class ListMoviesView(APIView):
#     """Displays all movies."""
#
#     allowed_method = ['GET']
#     serializer_class = MovieSerializer
#
#     def get(self, request):
#         queryset = Movie.objects.all()
#
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data, status=HTTP_200_OK)


# class ListMoviesFilteredView(APIView):
#     """API view for searching Movies."""
#
#     allowed_methods = ['GET']
#     serializer_class = MovieSerializer
#
#     def get(self, request):
#         queryset = Movie.objects.all()
#         result = []
#
#         # We can filter our movies by name
#         name = request.query_params.get('name', None)
#         if name is not None:
#             result = queryset.filter(name__icontains=name)
#
#         director = request.query_params.get('director', None)
#         if director is not None:
#             result = queryset.filter(director__icontains=director)
#
#         genre = request.query_params.get('genre', None)
#         if genre is not None:
#             result = queryset.filter(genre__name__icontains=genre)
#
#         rating = request.query_params.get('rating', None)
#         if rating is not None:
#             result = queryset.filter(imdb_score__gte=rating)
#
#         popularity = request.query_params.get('popularity', None)
#         if popularity is not None:
#             result = queryset.filter(popularity__gte=popularity)
#
#         if result == []:
#             return Response('Invalid query or no data available for this query.', status=HTTP_400_BAD_REQUEST)
#
#         serializer = self.serializer_class(result, many=True)
#         return Response(serializer.data, status=HTTP_200_OK)


# class List(ListAPIView):
#
#     allowed_methods = ['GET']
#     serializer_class = MovieSerializer
#     model = serializer_class.Meta.model
#     filter_fields = ('name', 'director', 'rating', 'genre', 'popularity')
#     paginate_by = 10
#
#     def get_queryset(self):
#         queryset = Movie.objects.all()
#         result = []
#
#         name = self.request.query_params.get('name', None)
#         if name is not None:
#             result = queryset.filter(name__icontains=name)
#
#         if result == []:
#             return result
#
#         return result.order_by('name')
