from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
#class GenreSerializer(serializers.ModelSerializer):
    """Serializer for Genre model"""

    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    """Serializer for Movie model"""

    genre = GenreSerializer(many=True, queryset=Genre.objects.all())
    #genre = GenreSerializer(many=True,  read_only=False, queryset=Genre.objects.all())
    class Meta:
            model = Movie
            fields = ('id','name', 'imdb_score', 'popularity', 'director', 'genre')
