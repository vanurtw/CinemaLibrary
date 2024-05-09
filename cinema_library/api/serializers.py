from rest_framework import serializers
from movie.models import Categories, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'tagline', 'rating', 'poster', 'genre']
        depth = 2

