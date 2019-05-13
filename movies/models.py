from __future__ import unicode_literals

from django.db import models

class Genre(models.Model):
    """Genre model : Table for movie Genres."""
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name

    objects = models.Manager()

class Movie(models.Model):
    """Movie model : model for Movies."""
    
    name = models.CharField(max_length=500)
    imdb_score = models.FloatField()
    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre, related_name='genre')

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name

    objects = models.Manager()
