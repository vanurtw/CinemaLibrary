from rest_framework import serializers
from movie.models import Categories


class HomeListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    tagline = serializers.CharField(max_length=255)
    rating = serializers.IntegerField()
    images = serializers.CharField(source='poster')
    # def update(self, instance, validated_data):


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'slug']


class YearSerializer(serializers.Serializer):
    data = serializers.DateTimeField(source='premiere')




