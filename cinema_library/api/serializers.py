from rest_framework import serializers
from movie.models import Categories, Movie, Genre, Reviews


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'tagline', 'rating', 'poster', 'genre', 'slug']
        depth = 2


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'description', 'slug']


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title', 'slug', 'description']


class RatingSerializers(serializers.Serializer):
    rating = serializers.CharField()


class ReviewsParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['name', 'email', 'text']


class ReviewsSerializers(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField('get_parent')
    rating = serializers.SerializerMethodField()

    def get_rating(self, instance):
        return instance.rating.rating

    def get_parent(self, instance):
        reviews_parent = instance.parents.all()
        return ReviewsParentSerializer(reviews_parent, many=True).data

    class Meta:
        model = Reviews
        fields = ['name', 'email', 'text', 'rating', 'parent']
